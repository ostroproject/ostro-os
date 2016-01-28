# Use the pre-generated keys for IMA signing.
IMA_EVM_KEY_DIR = "${IMA_EVM_BASE}/data/debug-keys"

# Enable local root access.
OSTRO_EXTRA_IMAGE_FEATURES += "autologin"

# Mark images as "development" by extending /etc/motd.
OSTRO_EXTRA_MOTD = "************************************\n*** This is a development image! ***\n*** Do not use in production.    ***\n************************************"
