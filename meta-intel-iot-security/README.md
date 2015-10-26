# meta-intel-iot-security

A collection of loosely related OpenEmbedded layers providing several
security technologies.

In general, the additional features must be explicitly enabled.
Merely adding the layers has little influence on the resulting
packages and images, therefore it is possible to build a distro where
security is an optional feature.

All layers can be used without the others, but then some features
might not be possible. For example, SecurityServer in
meta-security-framwork has a hard dependency on Smack from
meta-security-smack.

See the individual layer README's for further instructions.

# Copying

Unless noted otherwise, files are provided under the MIT license (see
COPYING.MIT).
