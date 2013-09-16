# give a different PACKAGE_ARCH to the recipes involved with opengl
python __anonymous () {
    provides = set((d.getVar("PROVIDES", True) or "").split())
    depends = set((d.getVar("DEPENDS", True) or "").split())

    glp = set([ "virtual/libgles1", "virtual/libgles2", "virtual/egl", "virtual/mesa" , "virtual/libgl"])
    if list(glp & (provides | depends)): # set union & intersection operations
        # matched
        d.appendVar("PACKAGE_ARCH", "${GLSUFFIX}")
    return
}
