FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}:"

COMPATIBLE_MACHINE_crownbay = "crownbay"
KMACHINE_crownbay  = "crownbay"
KBRANCH_crownbay  = "standard/default/crownbay"

COMPATIBLE_MACHINE_crownbay-noemgd = "crownbay-noemgd"
KMACHINE_crownbay-noemgd  = "crownbay"
KBRANCH_crownbay-noemgd  = "standard/default/crownbay"

SRCREV_machine_pn-linux-yocto_crownbay ?= "211fc7f4d10ec2b82b424286aabbaff9254b7cbd"
SRCREV_meta_pn-linux-yocto_crownbay ?= "514847185c78c07f52e02750fbe0a03ca3a31d8f"

SRCREV_machine_pn-linux-yocto_crownbay-noemgd ?= "211fc7f4d10ec2b82b424286aabbaff9254b7cbd"
SRCREV_meta_pn-linux-yocto_crownbay-noemgd ?= "514847185c78c07f52e02750fbe0a03ca3a31d8f"
