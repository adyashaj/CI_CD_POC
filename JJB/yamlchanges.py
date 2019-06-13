import fileinput, re, os



def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')


container_id=data.gerritContainerid
ip_address=data.gerritHostName
port_number=data.gerritHttpPort
password=data.gerrit_password
username=data.gerrit_admin
jenkinsName=data.jenkinsHostName
gerrit_container_name=data.gerritContainerName
gJUser=data.gerritUserName
gJUEmail=data.gerritEMail
gJCredentials=data.gerritCredentials



cmd = """ sudo sed -i -e "s/server-name:.*/server-name: Demo_Gerrit /" Gerrit_Trigger.yaml"""
os.system(cmd)


