import boto3
import json
from pathlib import Path

file_content = Path('tags.json').read_text()
file_content = json.loads(file_content)
tags = []

for tag_key in file_content:
    xx = {}
    xx["Key"] = tag_key
    xx["Value"] = file_content[tag_key]
    tags.append(xx)

crimefile = open('instance-ids.txt', 'r')
instance_ids = [line.strip() for line in crimefile.readlines()]

ec2 = boto3.resource('ec2')
ec2.create_tags( Resources = instance_ids, Tags = tags)


with open('output.txt', "w") as myfile:
    for instance in ec2.instances.all():
        myfile.write(instance.id + "   " + str(instance.tags) + '\n')