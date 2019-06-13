import fileinput, re, os,time

time.sleep(10)

#Read values from the variable file

def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')

print("Reading values from global_variables")


cmd = ("""ip route get 8.8.8.8""")
result = os.popen(cmd).read()
change = re.search('src (.+?) ',result)
ip_address = change.group(1)
#print (ip_address)

#artifactory_container_id= "a9f83555dae6"
artifactory_container_id=data.ArtifactoryContainerid

cmd1 = ("""docker inspect %s | jq -r '.[].NetworkSettings.Ports."8081/tcp"[]'""")%artifactory_container_id
result = os.popen(cmd1).read()
change = re.search('"HostPort": "(.+?)"',result)
port = change.group(1)
#print (port)

url="http://"+ip_address+":"+port+ "/artifactory"
filename = 'JenkinsVolume/org.jfrog.hudson.ArtifactoryBuilder.xml'
url="<url>" + url +"</url>"

#print(url)

with fileinput.FileInput(filename, inplace=True) as file:
    for line in file:
        print(re.sub("<url>\S+</url>",url, line), end = '')


print ("replaced")

#for jenkins.model.JenkinsLocationConfiguration.xml

jenkins_port='33333'

jenkinsUrl="http://"+ip_address+":"+jenkins_port
filename1 = 'JenkinsVolume/jenkins.model.JenkinsLocationConfiguration.xml'
jenkinsUrl="<jenkinsUrl>" + jenkinsUrl +"</jenkinsUrl>"
print(jenkinsUrl)

with fileinput.FileInput(filename1, inplace=True) as file:
    for line in file:
        print(re.sub("<jenkinsUrl>\S+</jenkinsUrl>",jenkinsUrl, line), end = '')

print("done")
