FILESEXTRAPATHS_prepend := "${THISDIR}/files/:"
SRC_URI_append_edison = " \
	file://obex_set_dbus_session_service.patch \
	"
