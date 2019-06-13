import os,re ,sys ,subprocess

#launching Gerrit Container

cmd1 =""" docker run -itd -p 32255:8080 -p 32256:29418 --name demogerritci gerritforge/gerrit-ubuntu16.04 """

result = os.popen(cmd1).read()
change = result[:12]
changeid1 =  ("""gerritContainerid= '%s'""")%change
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)

cmd = """ docker inspect %s | jq -r '.[].Mounts' """% (change)

result = os.popen(cmd).read()

#print result
test = (""" echo "%s" | sudo tee -a mount.txt """)% (result)
os.system(test)
line = subprocess.check_output("grep -n '/var/gerrit/db' /home/dragon/POC/mount.txt | cut -d: -f 1",shell=True)
li =int(line)
result12 =subprocess.check_output("awk \"NR==%d-1\" /home/dragon/POC/mount.txt "% li,shell=True)
print result12


change = re.search('/volumes/(.+?)/_data',result12)
changeid1 = change.group(1)

print changeid1

remove = "sudo rm -rf mount.txt"
os.system(remove)


home = "/home/dragon"
ch= os.chdir(home)

print ch

su = """sudo su"""
os.system(su)


path = "/home/dragon/POC/_data"
os.chdir(path)

print path 

volume_mount = """sudo cp -R * /var/lib/docker/volumes/%s/_data"""%changeid1
os.system(volume_mount)

print "mounted "

restart = """docker restart %s"""%(change)
os.system(restart)






#Jenkins container id


cmd3 ="""docker run -itd -p 32257:8080 --name demojenkinsci jenkins"""
result = os.popen(cmd3).read()
change1 = result[:12]
changeid2 =  ("""jenkinsContainerid= '%s'""")%change1
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid2)
os.system(test)


cmd1 = """docker inspect %s --format '{{.Mounts}}' """%(change1)

result = os.popen(cmd1).read()

change = re.search('/volumes/(.+?)/_data',result)
changeid = change.group(1)

print changeid

home = "/home/dragon"
ch= os.chdir(home)

print ch

su = """sudo su"""
os.system(su)


path = "/home/dragon/POC/gerrit_trigger/vol"
os.chdir(path)

print path 

volume_mount = """sudo cp -R * /var/lib/docker/volumes/%s/_data"""%changeid
os.system(volume_mount)

print "mounted "

restart = """docker restart %s"""%(change1)
os.system(restart)



