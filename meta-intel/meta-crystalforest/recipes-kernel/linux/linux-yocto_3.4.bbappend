FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"


COMPATIBLE_MACHINE_crystalforest-gladden = "crystalforest-gladden"
KMACHINE_crystalforest-gladden  = "crystalforest"
KBRANCH_crystalforest-gladden  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-gladden ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_crystalforest-gladden ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

COMPATIBLE_MACHINE_crystalforest-server = "crystalforest-server"
KMACHINE_crystalforest-server  = "crystalforest"
KBRANCH_crystalforest-server  = "standard/common-pc-64/crystalforest"

SRCREV_machine_pn-linux-yocto_crystalforest-server ?= "13809f2cfd9be0ce86bd486e1643f9b90bed6f4f"
SRCREV_meta_pn-linux-yocto_crystalforest-server ?= "f697e099bc76d5df3a307a5bc0cc25021dd6dfe0"

module_autoload_uio = "uio"

LINUX_VERSION = "3.4.28"
