#!/usr/bin/python
######################
#All users in group dev-box should also be in qa-box
######################

import os
from gdata.apps.groups.service import GroupsService


devbox = []
qabox = []

service = GroupsService(domain='google_hosted.domain_name',email='admin@email_address',password='admin_password')
service.ProgrammaticLogin()

#Start with dev-box
groups = 'dev-box'

members_feed = service.RetrieveAllMembers(groups, False)
emails = [user_dict['memberId'] for user_dict in members_feed]


for email in emails:
    username = email.split('@')[0]
    devbox.append(username)



#Next is qa-box
groups = 'qa-box'

members_feed = service.RetrieveAllMembers(groups, False)
emails = [user_dict['memberId'] for user_dict in members_feed]

for email in emails:
    username = email.split('@')[0]
    qabox.append(username)


groupName = 'qa-box'


dict = {}
for item in devbox:
    if item in qabox:
        dict[item] = 0 
    else:
        dict[item] = 1 

for k, v in dict.items(): 
    if v == 1:
       print k
       service.AddMemberToGroup( k, groupName  )
