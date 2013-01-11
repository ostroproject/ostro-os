
# The emgd binary driver also provides egl, gles1, gles2 library & headers.
# To avoid conflict disable egl, gles1, gles2 from meta-dri if the BSP image
# is bundling the emgd driver.

python __anonymous () {
    import re
    xserver = d.getVar('XSERVER', True)
    if xserver and 'emgd-driver-bin' in xserver.split(' '):
        extra_oeconf = d.getVar('EXTRA_OECONF', True).split()
        take_out = ["--enable-egl", "--enable-gles1", "--enable-gles2"]
        put_in = ["--disable-egl", "--disable-gles1", "--disable-gles2"]
        pattern = re.compile("--with-egl-platforms")
        new_extra_oeconf = [ ]
        for i in extra_oeconf:
            if ( i not in take_out ) and ( not pattern.match(i)):
                new_extra_oeconf.append(i)
        for i in put_in:
            new_extra_oeconf.append(i)

        d.setVar('EXTRA_OECONF', ' '.join(new_extra_oeconf))
        depends = d.getVar('DEPENDS', True)
        d.setVar('DEPENDS', depends + " emgd-driver-bin")
}
