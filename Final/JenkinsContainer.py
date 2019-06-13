import os,re ,sys ,subprocess , time

#Jenkins container id


cmd3 ="""docker run -itd -p 33333:8080 --name demojenkinsci jenkins_latest"""
result = os.popen(cmd3).read()
change1 = result[:12]
changeid2 =  ("""jenkinsContainerid= '%s'""")%change1
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid2)
os.system(test)

time.sleep(10)

import pdb;pdb.set_trace()

#cmd4 ="""docker stop %s"""% change1
#os.system(cmd4)

cmd1 = """docker inspect %s --format '{{.Mounts}}' """%(change1)

result = os.popen(cmd1).read()

change = re.search('/volumes/(.+?)/_data',result)
changeid = change.group(1)

print changeid


#su = """sudo su"""
#os.system(su)

getcwd = os.getcwd()
print getcwd

vol = "JenkinsVolume"
Jenkinsvol = (os.path.join(getcwd, vol))
print  Jenkinsvol
os.chdir(Jenkinsvol)

time.sleep(10)

volume_mount = """sudo cp -R * /var/lib/docker/volumes/%s/_data"""%changeid
os.system(volume_mount)

print "mounted "

time.sleep(10)

restart = """docker restart %s"""%(change1)
os.system(restart)



