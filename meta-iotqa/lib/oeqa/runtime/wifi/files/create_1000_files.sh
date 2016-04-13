mkdir -p /tmp/1000
i=1
while [ $i -lt 1001 ]
do
    touch /tmp/1000/$i
    i=`expr $i + 1`
done
