FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

python() {
    if ((d.getVar("PREFERRED_PROVIDER_virtual/kernel").startswith("linux-intel")) and
        (d.getVar("PREFERRED_VERSION_linux-intel").startswith("4.9"))):
        src_uri = d.getVar("SRC_URI")
        d.setVar("SRC_URI", src_uri +
                 " file://0001-zc-Force-4.10-get_user_pages_remote-API.patch")
}
