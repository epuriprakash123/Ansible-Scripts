import boto3
import sys
ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
 print instance.id, instance.state
 
 
#choose an amazon machine image 

instance = ec2.create_instances(
 ImageId='ami-1e299d7e',
 MinCount=1,
 MaxCount=1,
 InstanceType='t2.micro')
print instance[0].id 



#to terminate an instance
for instance_id in sys.argv[1:]:
 instance = ec2.Instance(instance_id)
 response = instance.terminate()
 print response
 
 
#list s3 buckets and their contents
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
 print bucket.name
 print "---"
 for item in bucket.objects.all():
 print "\t%s" % item.key
 
 
# creating a bucket
s3 = boto3.resource("s3")
for bucket_name in sys.argv[1:]:
 try:
 response = s3.create_bucket(Bucket=bucket_name)
 print response
 except Exception as error:
 print error


