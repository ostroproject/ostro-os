#!/bin/bash
# Author: lei.a.yang@intel.com
# This is FVT test for IOTOS-872


SEARCH_START="OpenSource base-files PLACEHOLDER"
COL_LIC="Requested License"
COL_SFW="Component Name"
COL_START="Component Name"
TABLE_COL=23
IOT_IP_SCAN_URL="https://iotos.fi.intel.com/jenkins/view/Code-Analysis/job/protexip-scan/lastSuccessfulBuild/artifact/.ci-dashboard/CC/IoT%20LinuxOS%20IP%20Plan.html"
TIMESTAMP=$(date +%Y%m%d-%H:%M:%S)
HEADER="license.head.$TIMESTAMP"
CONTENT="license.cont.$TIMESTAMP"
function usage()
{
    echo "Usage: $0 <image manifest file>"
    exit 1
}
function cleanup()
{
    [ -f $HEADER ] && rm $HEADER
    [ -f $CONTENT ] && rm $CONTENT
}

trap cleanup EXIT


curl -s "$IOT_IP_SCAN_URL" --insecure | ./scrape -be 'th' > $HEADER
curl -s "$IOT_IP_SCAN_URL" --insecure | ./scrape -be 'td' > $CONTENT

[ -z "$1" ] && echo "Error: No image manifest file input" && usage

COL_NUM=0
SEARCH_FLAG=0
COMPONENT_LOC=0
LICENSE_LOC=0
while read line; do
    if [ $SEARCH_FLAG -eq 0 ]; then
        echo $line | grep -q "$COL_START"
        if [ $? -eq 0 ]; then
            SEARCH_FLAG=1 && COL_NUM=$((COL_NUM+1)) 
            echo $line | grep -q "$COL_SFW"
            [ $? -eq 0 ] && COMPONENT_LOC=$COL_NUM
            echo $line | grep -q "$COL_LIC"
            [ $? -eq 0 ] && LICENSE_LOC=$COL_NUM
        fi
    else
        [[ $line =~ "th" ]] && COL_NUM=$((COL_NUM+1))
        echo $line | grep -q "$COL_SFW"
        [ $? -eq 0 ] && COMPONENT_LOC=$COL_NUM
        echo $line | grep -q "$COL_LIC"
        [ $? -eq 0 ] && LICENSE_LOC=$COL_NUM
    fi
done < $HEADER
[ $COL_NUM -le 0 ] && echo "Error: cannot get Column Number correctly" && exit 1
echo "Column Number: $COL_NUM"
[ $COMPONENT_LOC -le 0 ] && echo "Error: cannot get Component column number correctly" && exit 1
echo "Component location: $COMPONENT_LOC"
[ $LICENSE_LOC -le 0 ] && echo "Error: cannot get License column number correctly" && exit 1
echo "License location:   $LICENSE_LOC"

SEARCH_FLAG=0
SEARCH_COUNT=0
COMPONENT_LINE=""
#declare -A COMPONENT_LIST
COMP=""
while read line; do
    if [ $SEARCH_FLAG -eq 0 ]; then
        echo $line | grep -q "$SEARCH_START" 
        [ $? -eq 0 ] && SEARCH_FLAG=1 && SEARCH_COUNT=$((SEARCH_COUNT+1))
        [ $SEARCH_COUNT -gt 0 -a $SEARCH_COUNT -eq $COMPONENT_LOC ] && COMPONENT_LINE="$line" #&& echo "Component: $line"
    else
        echo "$line" | grep -q -E '^<td'
        if [ $? -eq 0 ]; then
            SEARCH_COUNT=$((SEARCH_COUNT+1))
            [ $SEARCH_COUNT -eq $COMPONENT_LOC ] && COMPONENT_LINE="$line" #&& echo "Component: $line" 
            if [ $SEARCH_COUNT -eq $LICENSE_LOC ]; then
                #echo "License: $line" 
                [[ "$line" =~ GNU.*3.0 ]] && COMP=$(echo "$COMPONENT_LINE" | awk -F ">" '{print $2}' | sed -e 's|</td||g' | sed 's/PLACEHOLDER//g' | sed 's/OpenSource//g' | sed -e 's/^ //g' | sed -e 's/ $//g')
                [ ! -z "$COMP" ] && COMPONENT_LIST=( "$COMP" "${COMPONENT_LIST[@]}" )
            fi
        else
            continue
        fi
    fi
    [ $SEARCH_COUNT -eq $COL_NUM ] && SEARCH_COUNT=0 && COMPONENT_LINE="" && COMP=""
done < $CONTENT

echo "list of component:"
echo "${COMPONENT_LIST[@]}"
echo "===================="

echo "There is ${#COMPONENT_LIST[@]} GPL/Less GPL/Affero GPL v3.0 components found from Ostro IP Plan"
echo "Check image manifest file to ensure the components are not built-in"

TC_RESULT="PASS"
for comp in ${COMPONENT_LIST[@]}; do
    echo "===  check $comp ==="
    cat "$1" | grep "$comp"
    [ $? -eq 0 ] && TC_RESULT="FAIL?" &&  echo "found suspected GPL/Less GPL/Affero GPL v3.0 component, need manual check"
done
echo "TEST_$TC_RESULT"
