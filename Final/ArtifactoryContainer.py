import os,re ,sys ,subprocess , time

#Artifactory container id


cmd3 ="""docker run -itd -p 34444:8081 --name demoartifactoryci docker.bintray.io/jfrog/artifactory-oss"""
result = os.popen(cmd3).read()
artifactory_container_id = result[:12]
changeid2 =  ("""ArtifactoryContainerid= '%s'""")%artifactory_container_id
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid2)
os.system(test)

time.sleep(30)

#cmd4 ="""docker stop %s"""% change1
#os.system(cmd4)

cmd1 = """docker inspect %s --format '{{.Mounts}}' """%(artifactory_container_id)

result = os.popen(cmd1).read()

change = re.search('/volumes/(.+?)/_data',result)
changeid = change.group(1)

print changeid


#su = """sudo su"""
#os.system(su)

getcwd = os.getcwd()
print getcwd


vol = "ArtifactoryVolume"
Artifactoryvol = (os.path.join(getcwd, vol))
print  Artifactoryvol
os.chdir(Artifactoryvol)

time.sleep(10)

volume_mount = """sudo cp -R * /var/lib/docker/volumes/%s/_data"""%changeid
os.system(volume_mount)

print "mounted "

time.sleep(10)

restart = """docker restart %s"""%(artifactory_container_id)
os.system(restart)



