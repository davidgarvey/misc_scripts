#!/usr/bin/python
#Create svn authz from google groups
#This is the authorization part. Authenication is seperate. 
#Note: This script needs somework. No backup of existing authz conf file
import ConfigParser
import os, datetime
from string import Template
from gdata.apps.groups.service import GroupsService

config_file='/path/to/pam_google.conf'
authz_path = '/path/to/svn/conf/authz'
groups = 'google-group'
application_name = 'svn-google-auth for google-group'
this_script = os.path.basename(__file__)

now = datetime.datetime.now()
header_start = "### Content generated by " + this_script + ": " + application_name +" ("
header_middle =  now.strftime("%Y/%m/%d %H:%M:%S")
header_end = ") ###\n\n"
header = header_start + header_middle + header_end
footer = "\n\n###Thank you for stopping by: " + application_name + " ###"

config = ConfigParser.ConfigParser()
config.read(config_file)


domain = config.get('googlepam','domain')
email=config.get('googlepam','admin-username')
password=config.get('googlepam','admin-password')
mail="%s@%s" %(email,domain)
members = []
service = GroupsService(domain=domain,email=mail,password=password)
service.ProgrammaticLogin()
members_feed = service.RetrieveAllMembers(groups, False)
emails = [user_dict['memberId'] for user_dict in members_feed]
for email in emails:
    username = email.split('@')[0]
    members.append(username)

string_members = ', '.join(members)

poop_stuff = '''
$header
[groups]
$groups = $string_members

[/]
@$groups = rw
$footer
'''

authz_template = Template(poop_stuff)
file = open(authz_path, 'w')
file.write(authz_template.substitute(locals()))




