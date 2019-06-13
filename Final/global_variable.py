import fileinput, re, os



def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')


gerrit_container_id=data.gerritContainerid
jenkins_container_id=data.jenkinsContainerid
artifactory_container_id=data.ArtifactoryContainerid

#jq ="""sudo apt-get install jq"""
#os.system(jq)


#To fetch Gerrit_trigger_name

Gerrit_Trigger_Name = ("""Gerrit_Trigger_Name= 'Demo_Gerrit1_new_test' """)

test = (""" echo "%s" | sudo tee -a variable.txt """)%Gerrit_Trigger_Name

os.system(test)


#To fetch ip_address of Host Server

cmd = ("""ip route get 8.8.8.8""")

result = os.popen(cmd).read()

change = re.search('src (.+?) ',result)
changeid = change.group(1)
changeid1 =  ("""gerritHostName= '%s'  """)%changeid

test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch Gerrit_Http_Port


cmd1 = ("""docker inspect %s | jq -r '.[].NetworkSettings.Ports."8080/tcp"[]'""")%gerrit_container_id
result = os.popen(cmd1).read()
change = re.search('"HostPort": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""gerritHttpPort= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)

#To fetch Gerrit_ssh_port

cmdssh = ("""docker inspect %s | jq -r '.[].NetworkSettings.Ports."29418/tcp"[]'""")%gerrit_container_id
result = os.popen(cmdssh).read()
change = re.search('"HostPort": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""gerritSshPort= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)

#To fetch Gerrit_Admin

gerrit_admin= 'admin'

gerritAdmin=("""gerrit_admin= 'admin'""")

test = (""" echo "%s" | sudo tee -a variable.txt """)%gerritAdmin

os.system(test)

#To fetch Gerrit_password

gerrit_password= 'admin'

gerritPassword=("""gerrit_password= '%s' """)%gerrit_password

test = (""" echo "%s" | sudo tee -a variable.txt """)%gerritPassword

os.system(test)
 
#To fetch Gerrit_username

gerritUserName= 'Jenkins'

gerrit_username=("""gerritUserName= 'Jenkins'""")

test = (""" echo "%s" | sudo tee -a variable.txt """)%gerrit_username

os.system(test)
 
#To fetch Gerrit_email

gerritEMail= 'jenkins@example.com'

gerrit_Email=("""gerritEMail= 'jenkins@example.com'""")

test = (""" echo "%s" | sudo tee -a variable.txt """)%gerrit_Email

os.system(test)

#To fetch Gerrit_credentials

gerritCredentials= 'jenkins'

gerrit_Credentials=("""gerritCredentials= 'jenkins'""")

test = (""" echo "%s" | sudo tee -a variable.txt """)%gerrit_Credentials

os.system(test)

#To fetch Gerrit_containerip

cmd1 = ("""docker inspect %s | grep '"IPAddress"' | head -n 1""")%gerrit_container_id
result = os.popen(cmd1).read()
change = re.search('"IPAddress": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""gerritContainerIP= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch Gerrit Hostname

cmd1 = ("""docker inspect %s --format='{{.Name}} '""")%gerrit_container_id
result = os.popen(cmd1).read()
change = re.search('/(.+?) ',result)
changeid = change.group(1)
changeid1 =  ("""gerritContainerName= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)

#To fetch Jenkins_port

cmd1 = ("""docker inspect %s | jq -r '.[].NetworkSettings.Ports."8080/tcp"[]'""")%jenkins_container_id
result = os.popen(cmd1).read()
change = re.search('"HostPort": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""jenkinsSshPort= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch jenkinsHostName


cmd1 = ("""docker inspect %s --format='{{.Name}} '""")%jenkins_container_id
result = os.popen(cmd1).read()
change = re.search('/(.+?) ',result)
changeid = change.group(1)
changeid1 =  ("""jenkinsHostName= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch Jenkins_containerip

cmd1 = ("""docker inspect %s | grep '"IPAddress"' | head -n 1""")%jenkins_container_id
result = os.popen(cmd1).read()
change = re.search('"IPAddress": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""jenkinsContainerIP= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch Artifactory_port

cmd1 = ("""docker inspect %s | jq -r '.[].NetworkSettings.Ports."8081/tcp"[]'""")%artifactory_container_id
result = os.popen(cmd1).read()
change = re.search('"HostPort": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""ArtifactorySshPort= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch ArtifactoryHostName


cmd1 = ("""docker inspect %s --format='{{.Name}} '""")%artifactory_container_id
result = os.popen(cmd1).read()
change = re.search('/(.+?) ',result)
changeid = change.group(1)
changeid1 =  ("""ArtifactoryHostName= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)


#To fetch Artifactory_containerip

cmd1 = ("""docker inspect %s | grep '"IPAddress"' | head -n 1""")%artifactory_container_id
result = os.popen(cmd1).read()
change = re.search('"IPAddress": "(.+?)"',result)
changeid = change.group(1)
changeid1 =  ("""ArtifactoryContainerIP= '%s'""")%changeid
test = (""" echo "%s" | sudo tee -a variable.txt """)% (changeid1)
os.system(test)
