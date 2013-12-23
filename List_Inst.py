import boto.ec2

Region ='<region>' #something like 'us-west-1'
User = '<user>' #user setup in aws

conn = boto.ec2.connect_to_region(Region) 
reservations = conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for inst in instances:
    if User in inst.tags:
        print "Name:%s ID:%s  IP:%s State:%s" %(inst.tags['Name'],inst,inst.public_dns_name,inst.state)