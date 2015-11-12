FILESEXTRAPATHS_prepend := "${THISDIR}/policy:"

# List of files in the "policy" directory. They completely replace the upstream
# policy files.
SECURITY_MANAGER_POLICY = " \
privilege-group.list \
usertype-admin.profile \
usertype-guest.profile \
usertype-normal.profile \
usertype-system.profile \
CMakeLists.txt \
InternetAccess-template.smack \
LocalNetworkAccess-template.smack \
"

# SecurityManager tries to add additional groups as defined by our
# profiles. We do not really use any of these groups yet, but need to
# create them anyway to avoid warnings.
#
# It would be nicer if this worked regardless of the .bb recipe's
# GROUPADD_PARAM_${PN}-policy value (currently empty, but perhaps
# that'll change). It doesn't, because adding a redundant trailing
# semi-colon triggers a failing attempt to add a group without names.
GROUPADD_PARAM_${PN}-policy =. " \
-r priv-conquery; \
-r priv-conmanage; \
-r priv-credmanage; \
-r priv-appmanage; \
-r priv-powermanage; \
-r priv-lanaccess; \
-r priv-netaccess; \
-r priv-senaccess; \
-r priv-streamaccess; \
-r priv-geoaccess; \
-r priv-shareaccess; \
-r priv-extaccess \
"
USERADD_PACKAGES += "${PN}-policy"
inherit useradd
