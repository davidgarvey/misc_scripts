import boto.ec2
import sys
import time

Region = '<region>' #Something like 'us-west-1'
Placement = '<region placement>' #Something like 'us-west-1b'
User = '<user>' # User with access to aws
Ami = 'ami for user' # something like 'ami-xxxxxx'
Instance_Type = 't1.micro' # The size of instance the user can create
SG = ['<sec group>'] # the security group for user
dev_sda = boto.ec2.blockdevicemapping.EBSBlockDeviceType()
dev_sda.size = 100 # size in Gigabytes


#Setup block device size object (Note: for linux you need to resize disk once started resize2fs /dev/root-dev)
bdm = boto.ec2.blockdevicemapping.BlockDeviceMapping()
bdm['/dev/sda'] = dev_sda




conn = boto.ec2.connect_to_region(Region) 
reservations = conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for inst in instances:
    if User in inst.tags:
        print "Name:%s ID:%s  IP:%s State:%s" %(inst.tags['Name'],inst,inst.public_dns_name,inst.state)

print "PLEASE ENTER A NAME FOR YOUR NEW BOX"
name = raw_input("Enter your host name: ")
name = name.replace('\n','')
print name


reservation = conn.run_instances(Ami, instance_type=Instance_Type, key_name=User, placement=Placement, security_groups=SG, block_device_map = bdm)
instance = reservation.instances[0]
status = instance.update()
while status == 'pending':
    print status
    time.sleep(10)
    status = instance.update()
if status == 'running':
    instance.add_tag(User,'true') # I use the username for the tag, so the user only manages boxes they have created
    instance.add_tag('Name',name)
else:
    print('Instance status: ' + status)
