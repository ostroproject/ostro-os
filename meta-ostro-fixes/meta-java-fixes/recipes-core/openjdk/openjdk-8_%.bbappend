# Set openjdk to provide java2-runtime so that rhino can be
# added to image without pulling cacao or openjdk-7 as well
RPROVIDES_${JDKPN}-jre_append = " java2-runtime"

