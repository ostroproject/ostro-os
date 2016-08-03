SUMMARY = "Central RMC Database"
DESCRIPTION = "Generate a centralized RMC database for RMC feature. \
Fingerprints and data for all boards supported are specified by variable \
RMC_BOARD_DATA_DIRS which is a list of top directories that contains \
subdirectories for boards. Developers can add their top directories by appending \
them to this variable in a rmc-db.bbappend.Refer to rmc-db bbclass for more \
information."

LICENSE = "MIT"

LIC_FILES_CHKSUM = "file://${COREBASE}/LICENSE;md5=4d92cd373abda3937c2bc47fbc49d690"

S = "${WORKDIR}"

inherit rmc-db

RMC_BOARD_DATA_DIRS_append := " ${THISDIR}/boards/"
RMC_DB_DIR = "${WORKDIR}/db"

# Let sstate be aware of change in any added board directories
do_generate_rmc_db[file-checksums] = "${@get_rmc_top_dirs_list(d)}"

# derived from get_lic_checksum_file_list(d) in base.bbclass in OE
def get_rmc_top_dirs_list(d):
    dirlist = []
    dirs = d.getVar("RMC_BOARD_DATA_DIRS", True) or ''
    topdirs = dirs.split()
    for each in topdirs:
        dirlist.append(each + ":" + str(os.path.exists(each)))
    return " ".join(dirlist)

do_generate_rmc_db () {
	rmc_generate_db "${RMC_BOARD_DATA_DIRS}" "${RMC_DB_DIR}"/rmc.db
}

addtask generate_rmc_db  after do_compile

inherit deploy

do_deploy () {
	if [ -f ${RMC_DB_DIR}/rmc.db ]; then
		install -m 0400 ${RMC_DB_DIR}/rmc.db ${DEPLOYDIR}
	else
		echo "Warning: no RMC central database found, skip deployment."
	fi
}

addtask deploy after do_generate_rmc_db
