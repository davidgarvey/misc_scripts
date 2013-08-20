#!/usr/bin/python
import ConfigParser
import os
from subprocess import Popen, PIPE
from gdata.apps.groups.service import GroupsService
#
#Add new users after google group has been updated
#
config_file='/path/to/pam_google.conf'

def addUser(userName):
    status = os.system("useradd -g dev %s"%(userName))
    if status <> 0:
        print "useradd Failed for user: " + userName
        sys.exit()
    else:
        print "Successful useradd for user: " + userName

config = ConfigParser.ConfigParser()
config.read(config_file)

groups = config.get('googlepam','group')
domain = config.get('googlepam','domain')
email=config.get('googlepam','admin-username')
password=config.get('googlepam','admin-password')
mail="%s@%s" %(email,domain)

service = GroupsService(domain=domain,email=mail,password=password)
service.ProgrammaticLogin()
members_feed = service.RetrieveAllMembers(groups, False)
emails = [user_dict['memberId'] for user_dict in members_feed]
for email in emails:
    username = email.split('@')[0]
    #Check if the users in google group exist on this box.
    user_exists = 'id -u %s' %username
    p = Popen(user_exists, stderr=PIPE, stdout=PIPE, shell=True)
    output, errors = p.communicate()
    if p.returncode == 1:
        addUser(username)
        print p.returncode
        print username

