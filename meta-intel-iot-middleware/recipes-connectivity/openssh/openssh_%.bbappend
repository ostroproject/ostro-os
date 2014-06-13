inherit systemd

# make the sshdgenkeys service required by multi-user.target to make it generate keys on first boot
do_compile_append() {
  echo "[Install]
WantedBy=multi-user.target" >> ${WORKDIR}/sshdgenkeys.service
}

SYSTEMD_SERVICE_${PN}-sshd = "sshd.socket sshdgenkeys.service"
