import boto3
import json
from pathlib import Path

# -- READING TAGS.JSON FILE 
file_content = Path('tags.json').read_text()
file_content = json.loads(file_content)
tags = []

# -- CONVERTING FILE CONTENT TO PROPER JSON FORMAT
for tag_key in file_content:
    xx = {}
    xx["Key"] = tag_key
    xx["Value"] = file_content[tag_key]
    tags.append(xx)

# -- READING A FILE WITH INSTANCE IDS and ADDING THEM TO THE LIST "INSTANCE_IDS"
instance_idsFile = open('instance-ids.txt', 'r')
instance_ids = [line.strip() for line in instance_idsFile.readlines()]

# -- CREATING TAGS VIA BOTO3
ec2 = boto3.resource('ec2')
ec2.create_tags( Resources = instance_ids, Tags = tags)

# -- WRITING ALL INSTANCE IDS and TAGS INTO OUTPUT.TXT FILE
with open('output.txt', "w") as myfile:
    for instance in ec2.instances.all():
        myfile.write(instance.id + "   " + str(instance.tags) + '\n')
print('Done')