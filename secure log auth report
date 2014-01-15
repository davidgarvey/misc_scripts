#!/usr/bin/python
######################################################
# This python code goes into the /var/log dir and finds
# all logs of logtype and looks for strings defined in
# keywork list and applys a regex to them to write a csv
# file.
######################################################


import re
import os
logdir='/var/log/'
logtype = 'secure'
keywords = ['Accepted publickey','Accepted password','Failed password']

#Get all logs cuz in this case they are rotated weekly with 4 logs total, this gives me monthly...

logfiles = sorted([ f for f in os.listdir(logdir) if f.startswith(logtype)])
logfiles.sort(key=lambda s: os.path.getmtime(os.path.join(logdir, s)))
print " month , day , time , host , ipaddress , string "

for file in logfiles:
    file = "%s%s" %(logdir,file)
    fd = open(file, "r")
    for line in fd:
        m = re.match(r"(?P<month>\w+)\s+(?P<day>\d+)\s(?P<time>[\d+\:]+)\s(?P<host>\w+\W?\S+)\s.*\:(?P<string>[\w+\s+]+)\s(?P<ipadd>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})?)", line)
        for keyword in keywords:
            if keyword in line:
                ipadd = m.group('ipadd')
                month = m.group('month')
                day = m.group('day')
                time = m.group('time')
                host = m.group('host')
                string = m.group('string')
                print month + "," + day + "," + time + "," + host + "," + ipadd + "," + string 
               
    fd.close()
