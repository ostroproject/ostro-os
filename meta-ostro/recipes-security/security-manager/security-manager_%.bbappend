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
