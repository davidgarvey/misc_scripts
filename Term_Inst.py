import boto.ec2

Region = '<region>' # Something like 'us-west-1'
User = '<user>' # User account



conn = boto.ec2.connect_to_region(Region)
reservations = conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for inst in instances:
    if User in inst.tags:
        print "Name:%s ID:%s  IP:%s State:%s" %(inst.tags['Name'],inst,inst.public_dns_name,inst.state)




print "PLEASE ENTER INSTANCE ID OF BOX YOU WISH TO TERMINATE"
instID = raw_input("Enter your Instance ID: ")
instID = instID.replace('\n','')
print instID

conn.terminate_instances(instance_ids=[instID])
