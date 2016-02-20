# Use this class in BBCLASSEXTEND of an image recipe to define
# additional variations of the base image where certain image features
# are turned on or off.
#
# Features get modified after parsing the image recipe. This implies
# that constructs in the recipe which check the current state of
# ${IMAGE_FEATURES} during parsing will not have the expected effect:
# * inherit with varying class names
# * := assignments
#
# The specific modifications must be listed as comma-separated
# parameters to the class in BBCLASSEXTEND. In the virtual image
# recipes, a hyphen will be used instead of the comma. To disable
# a feature, use "no" or "no-" as prefix in the parameter.
#
# Parameters can also be aliases for other parameters or features.
# This allows creating recipes with a short suffix when the actual
# modifications are large and/or change over time.
#
# Example for core-image-minimal.bb:
#   IMAGE_VARIANT[dev] = "tools-debug tools-profile"
#   BBCLASSEXTEND = "imagevariant:ptest-pkgs imagevariant:tools-debug,no-debug-tweaks imagevariant=dev"
#   ->
#   core-image-minimal-ptest-pkgs (ptest-pkgs enabled)
#   core-image-minimal-tools-debug-no-debug-tweaks (debug-tweaks disabled)
#   core-image-minimal-dev (with tools-debug and tools-profile image features enabled)

python imagevariant_virtclass_handler () {
    pn = e.data.getVar("PN", True)
    cls = e.data.getVar("BBEXTENDCURR", True)
    variant = e.data.getVar("BBEXTENDVARIANT", True)
    # multilib.bbclass checks with "if ... return" for historic
    # reasons. Since OE-core 2.0, we are guaranteed to get called only
    # when these values are set, unless the user made a mistake.
    if cls != 'imagevariant':
	return
    if not variant:
        bb.fatal('BBCLASSEXTEND=imagevariant must be used with parameters, as in BBCLASSEXTEND=imagevariant:no-debug-tweaks,tools-profile')

    parameters = variant.split(',')

    # Rename the virtual recipe to create the desired image variant.
    pn = pn + '-' + '-'.join(parameters)
    e.data.setVar("PN", pn)

    # Expand parameter aliases, recursively.
    def expand(parameters):
        modified = []
        for parameter in parameters:
            alias = e.data.getVarFlag('IMAGE_VARIANT', parameter, True)
            if alias is not None:
                modified.extend(expand(alias.split()))
            else:
                modified.append(parameter)
        return modified
    parameters = expand(parameters)

    # Validate parameters and apply them to IMAGE_FEATURES.
    valid_features = set(e.data.getVarFlag('IMAGE_FEATURES', 'validitems', True).split())
    current_features = set(e.data.getVar('IMAGE_FEATURES', True).split())
    def remove_feature(word):
        # The feature to be removed is not necessarily enabled.
        is_active = word in current_features
        if is_active:
            current_features.remove(word)
        # Tell caller whether we are sure that 'word' represented a feature.
        # If so, no further action is needed on the parameter.
        return is_active or word in valid_features

    for parameter in parameters:
        if parameter in valid_features:
            # Enables a feature.
            current_features.add(parameter)
        elif parameter.startswith('no') and remove_feature(parameter[2:]) or \
             parameter.startswith('no-') and remove_feature(parameter[3:]):
             # Parameter was used to disable a feature.
             pass
        else:
             bb.fatal("imagevariant parameter '%s' neither enables nor disables any known feature" % parameter)
    e.data.setVar('IMAGE_FEATURES', ' '.join(current_features))
}

addhandler imagevariant_virtclass_handler
imagevariant_virtclass_handler[eventmask] = "bb.event.RecipePreFinalise"
