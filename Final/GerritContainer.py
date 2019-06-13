import os,re ,sys ,subprocess, time

#launching Gerrit Container

cmd1 =""" docker run -itd -p 32222:8080 -p 32223:29418 --name demogerritci gerritforge/gerrit-ubuntu16.04 """

result = os.popen(cmd1).read()
change = result[:12]
changeid1 =  ("""gerritContainerid= '%s'""")%change
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)

time.sleep(30)

print """ ******************** Gerrit Container is Launched *************************** """

#Getting Container Volume

cmd = """ docker inspect %s | jq -r '.[].Mounts' """% change

result = os.popen(cmd).read()

test = (""" echo "%s" | sudo tee -a mount.txt """)% (result)
os.system(test)

line = subprocess.check_output("grep -n '/var/gerrit/db' mount.txt | cut -d: -f 1",shell=True)
print line

li =int(line)
result12 =subprocess.check_output("awk \"NR==%d-1\" mount.txt "% li,shell=True)
print result12


changevol = re.search('/volumes/(.+?)/_data',result12)
changeidvol = changevol.group(1)

print changeidvol

remove = "sudo rm -rf mount.txt"
os.system(remove)

# Mounting Gerrit Volume

#su  = """sudo su"""
#os.system(su)

getcwd = os.getcwd()
print getcwd




vol = "GerritVolume"
Gerritvol = (os.path.join(getcwd, vol))
print  Gerritvol
os.chdir(Gerritvol)

time.sleep(10)

volume_mount = """sudo cp -R * /var/lib/docker/volumes/%s/_data"""%changeidvol
os.system(volume_mount)

print " ********* Gerrit Volume is mounted ************ "

restart = """docker restart %s"""%(change)
os.system(restart) 


time.sleep(10)
