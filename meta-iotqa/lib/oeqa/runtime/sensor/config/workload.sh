#!/bin/sh
i=1
cp -r /var /opt/var
cp -r /var /opt/var/var
cp -r /var /opt/var/var/var
cp -r /var /opt/var/var/var
cp -r /var /opt/var/var/var/var
cp -r /var /opt/var/var/var/var/var
cd /opt
while [ $i -le 60 ]
      do      
        echo "succeed"
        #mkdir /opt/var
        tar -zcvf var.gz.tar ./var
        rm -rf ./var
        tar -zxvf var.gz.tar
        i=$((i+1))
      done
rm -rf /opt/var*
