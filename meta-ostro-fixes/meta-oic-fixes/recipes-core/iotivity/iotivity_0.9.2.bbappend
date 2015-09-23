SRC_URI += "file://0001-ocpayload-free-arr.patch \
            file://0002-ocstack.c-terminate-strings.patch \
            file://0003-ocpayload-free-out-if-cannot-allocate.patch \
            file://0004-oc-client-server-coll-don-t-call-putPayload-more-tha.patch \
            file://0005-psinterface-objects-created-with-cJSON_Duplicate-mus.patch \
            file://0006-ocservercoll-always-free-payload.patch \
            file://0007-ResourceInitException-don-t-return-dangling-pointer.patch \
            file://0001-iotivity-fixes-uninitialized-variables-usage.patch \
           "

FILESEXTRAPATHS_prepend := "${THISDIR}/files:"
