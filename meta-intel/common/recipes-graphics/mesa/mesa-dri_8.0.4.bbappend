# Temporary avoid warnings of duplicate files providers until
# mesa-dri & emgd-driver-bin recipes are fixed
SSTATE_DUPWHITELIST += "${STAGING_INCDIR}/KHR ${STAGING_INCDIR}/EGL \
                        ${STAGING_INCDIR}/GLES ${STAGING_INCDIR}/GLES2"

