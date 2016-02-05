
#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ(2.59)

AC_INIT([example-app-c], [0.1])

AC_CONFIG_SRCDIR([src])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_HEADER([src/config.h])
AM_INIT_AUTOMAKE([-Wno-portability subdir-objects foreign])

AC_SUBST(ACLOCAL_AMFLAGS, "-I m4")
AC_SUBST(VERSION)

# Disable static libraries.
AC_DISABLE_STATIC

# Checks for programs.
AC_PROG_CC
AC_PROG_CC_C99
AC_PROG_AWK
AC_PROG_INSTALL
AM_PROG_CC_C_O
AM_PROG_LIBTOOL

# Make first invocation of PKG_CHECK_MODULES 'if-then-else-fi'-safe.
PKG_PROG_PKG_CONFIG

# Checks for header files.
AC_PATH_X
AC_CHECK_HEADERS([stdio.h])

AC_ARG_WITH(package-name,
            [  --with-package-name      package name],
            [pkg_name=${with_package_name}], AC_MSG_ERROR([no package-name specified]))
AC_SUBST(PACKAGE_NAME, [$pkg_name])

AC_ARG_WITH(install-path, 
            [  --with-install-path      where the app. files should go],
            [install_path="${with_install_path}"], AC_MSG_ERROR([no install-path provided]))
AC_SUBST(INSTALL_PATH, [$install_path])

AC_ARG_WITH(manifest-path, 
            [  --with-manifest-path      where the manifest file should go],
            [manifest_path="${with_manifest_path}"], AC_MSG_ERROR([no manifest-path provided]))
AC_SUBST(MANIFEST_PATH, [$manifest_path])



# Allow substitution for LIBDIR and SYSCONFDIR.
AC_MSG_CHECKING([libdir])
AC_MSG_RESULT([$libdir])
AC_SUBST(LIBDIR, [$libdir])
AC_MSG_CHECKING([sysconfdir])
AC_MSG_RESULT([$sysconfdir])
AC_SUBST(SYSCONFDIR, [$sysconfdir])

# Shave by default.
SHAVE_INIT([build-aux], [enable])

# Generate output.
AC_CONFIG_FILES([build-aux/shave
                 build-aux/shave-libtool
                 Makefile
                 src/Makefile
                 src/manifest
		 ])
AC_OUTPUT

# Display the configuration.
echo "----- configuration -----"
echo "package_name: ${PACKAGE_NAME}"
echo "install_path: ${INSTALL_PATH}"
echo "manifest_path: ${MANIFEST_PATH}"
