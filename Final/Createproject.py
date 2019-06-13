import fileinput, re, os, time




def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')


gituser = """sudo git config --global user.name "Jenkins" """
os.system(gituser)



gituserEmail= " sudo git config --global user.email jenkins@example.com"
os.system(gituserEmail)



username=data.gerritUserName
password=data.gerritCredentials
ip_address=data.gerritHostName
port_number=data.gerritHttpPort
gerrit_container_name=data.gerritContainerName
# Creating_Gerrit_Project




print """ please refresh your gerrit page """

time.sleep(30)

create_project = """curl -X PUT -H 'Content-Type: application/json' -u '%s:%s'  -i 'http://%s:%s/a/projects/Gerrit_Trigger' --data ' {
    "description": "This is a demo project.",
    "submit_type": "CHERRY_PICK",
    "owners": [
      "Administrators",
      "Non-Interactive Users"
         ]
  }'"""% (username , password , ip_address , port_number )

result = os.popen(create_project).read()

print result

# Restart_Gerrit


#restart_docker = "docker restart %s"% (gerrit_container_name)

#os.system (restart_docker)

