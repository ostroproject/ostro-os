# Class that allows you to restrict the recipes brought from a layer to
# a specified list. This is similar in operation to blacklist.bbclass
# but note the difference in how PNWHITELIST is set - we don't use varflags
# here, the recipe name goes in the value and we use an override for the
# layer name (although this is not strictly required - you can have one
# PNWHITELIST value shared by all of the layers specified in
# PNWHITELIST_LAYERS). The layer name used here is actually the name that
# gets added to BBFILE_COLLECTIONS in the layer's layer.conf, which may
# differ from how the layer is otherwise known - e.g. meta-oe uses
# "openembedded-layer".
#
# INHERIT += "whitelist"
# PNWHITELIST_LAYERS = "layername"
# PNWHITELIST_layername = "recipe1 recipe2"
#
# If you would prefer to set a reason message other than the default, you
# can do so:
#
# PNWHITELIST_REASON_layername = "not supported by ${DISTRO}"

python() {
    layer = bb.utils.get_file_layer(d.getVar('FILE', True), d)
    if layer:
        layers = (d.getVar('PNWHITELIST_LAYERS', True) or '').split()
        if layer in layers:
            localdata = bb.data.createCopy(d)
            localdata.setVar('OVERRIDES', layer)
            whitelist = (localdata.getVar('PNWHITELIST', True) or '').split()
            if not (d.getVar('PN', True) in whitelist or d.getVar('BPN', True) in whitelist):
                reason = localdata.getVar('PNWHITELIST_REASON', True)
                if not reason:
                    reason = 'not in PNWHITELIST for layer %s' % layer
                raise bb.parse.SkipRecipe(reason)
}
