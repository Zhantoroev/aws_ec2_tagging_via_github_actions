# Python for tagging ec2 instances in AWS REGION


In **instance-ids** file you should write _ec2 instance ids_. Write ids **line by line** , each should be on a new line with out any comas and white-spaces.
**Example content of instance-ids.txt:**
<pre>i-0232aae72b3e6d5a5
i-01272b45ee3232334
i-0dab2b4234ffdsfd2
i-0534543ee3e6fda36
</pre>
\
In **tags.json** write your tags which should be _added of updated_ in JSON format. It should be like tag_key : tag_value.
Example content of tags.json file:
<pre>{
    "Env" : "PROD",
    "Owner" : "Zhantoroev"
}
</pre>

For **Github Actions** there is a main.yml file. In line 4, for cron job you can specify a time to schedule run this python code. 
Lines 18-21. Add your credentials like AWS ACCESS KEY, SECRET ACCESS KEY and REGION NAME to Github Secrets.

`

### **NOTE:** Python code will work on the region according to your credentials (REGION NAME)
\
\
\
`
## RUN **without** Github Actions: 
<pre>
clone repo and open it. In terminal type 
<pre>
python tagging_ec2.py
</pre>
If everything works fine, it will print "done"
</pre>

## RUN **with** Github Actions:
<pre>
* Copy repo 
* At first add your credentials to secrets on github
* Change main.yml on line 19-21 if you need it
* If you wish, you can change line 4 cronjob time
* Push your code and it will run according to cronjob 
</pre>