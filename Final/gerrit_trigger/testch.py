import fileinput, re, os

#Read values from the variable file

def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')

print("Reading values from global_variables")

Trigger_name=data.Gerrit_Trigger_Name
gerrit_Host_Name=data.gerritHostName
gerrit_Ssh_Port=data.gerritSshPort
gerrit_Http_Port=data.gerritHttpPort
gerrit_User_Name=data.gerritUserName
gerrit_Email=data.gerritEMail
jenkinsHostName=str(data.jenkinsHostName)
#gerritFrontEndUrl=data.gerritFrontEndUrl
gerritFrontEndUrl="http://"+gerrit_Host_Name+":"+gerrit_Http_Port

#print(jenkinsHostName)


# Change Gerrit_trigger.xml file

filename = 'gerrit-trigger.xml'

trigger_name="<name>" + Trigger_name + "</name>"
gerrit_host_name="<gerritHostName>" + gerrit_Host_Name + "</gerritHostName>"
gerrit_ssh_port="<gerritSshPort>" + gerrit_Ssh_Port + "</gerritSshPort>"
gerrit_user_name="<gerritUserName>" + gerrit_User_Name + "</gerritUserName>"
gerrit_user_email="<gerritEMail>" + gerrit_Email + "</gerritEMail>"
gerritFrontEndUrl="<gerritFrontEndUrl>" + gerritFrontEndUrl + "</gerritFrontEndUrl>"
#gerritFrontEndUrl="<gerritFrontEndUrl>" + gerritFrontEndUrl +"</gerritFrontEndUrl>"

print(gerritFrontEndUrl)

#print(trigger_name)
#print(gerrit_host_name)
#print(gerritSshPort)
#print(gerritUserName)
#print(gerritEmail)

with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("<name>\S+</name>", trigger_name, line), end = '')
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("<gerritHostName>\S+</gerritHostName>", gerrit_host_name, line), end = '')
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("<gerritSshPort>\S+</gerritSshPort>", gerrit_ssh_port, line), end = '')
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("<gerritUserName>\S+</gerritUserName>", gerrit_user_name, line), end = '')
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("<gerritEMail>\S+</gerritEMail>", gerrit_user_email, line), end = '')
with fileinput.FileInput(filename, inplace=True,backup='.bak') as file:
    for line in file:
        print(re.sub("<gerritFrontEndUrl>\S+</gerritFrontEndUrl>", gerritFrontEndUrl, line), end = '')
#with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
#    for line in file:
#        print(re.sub("<gerritFrontEndUrl>\S+</gerritFrontEndUrl>", gerritFrontEndUrl, line), end = '')

cmd="docker exec -i %s  sh -c 'cat > /var/jenkins_home/gerrit-trigger.xml'< ./gerrit-trigger.xml"% (jenkinsHostName)
os.system(cmd)
cmd1="docker restart %s"% (jenkinsHostName)
os.system(cmd1)
print("restarted")
