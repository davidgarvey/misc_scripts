#!/bin/bash

limit=180 #limit in secs.

results=`mysql -N -u mysqluser -p'secret' -e "show processlist" | awk '{print$6}' | xargs`

array=($results)
 

status=0
for i in "${array[@]}";do

if [ $i -gt $limit ]; then
#echo $i
status=1
fi

done

if [ $status -gt "0" ]; then
echo "Long Running Proc: critical"
exit 2
else
echo "No Long running Procs: OK"
exit 0
fi
