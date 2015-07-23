
TARGET_FILES ?= ""
NATIVE_FILES ?= ""
do_copybin() {
    target_dir=${DEPLOY_DIR}/files/${MACHINE}
    mkdir -p ${target_dir}
    if [ ! -z "${TARGET_FILES}" ]; then
       cp -rf ${TARGET_FILES} ${target_dir}/
    fi
    native_dir=${DEPLOY_DIR}/files/native/${BUILD_ARCH}
    mkdir -p ${native_dir}
    if [ ! -z "${NATIVE_FILES}" ]; then
       cp -rf ${NATIVE_FILES} ${native_dir}/
    fi
}
addtask do_copybin after do_compile before do_install
#addtask do_copybin after do_install
