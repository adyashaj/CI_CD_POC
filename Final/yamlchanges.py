import fileinput, re, os



def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')

server_name=data.Gerrit_Trigger_Name
ip_address=data.gerritHostName
port=data.gerritHttpPort
jenkinsport=data.jenkinsSshPort

print jenkinsport

art_port=data.ArtifactorySshPort

cmdser = """ sudo sed -i -e "s/server-name:.*/server-name: %s /"  Test_Gerrit.yaml"""% (server_name)
os.system(cmdser)


server = """ '%s',"""%(server_name)
cmd = """ sudo sed -i -e "s/serverName:.*/serverName: %s /"  Test_Gerrit.yaml"""% (server)
os.system(cmd)

url = """'http:\/\/%s:%s\/Gerrit_Trigger.git']]]) """%(ip_address , port)
cmd1 = """sudo sed -i -e  "s/url: .*/url: %s /"  Test_Gerrit.yaml"""% (url)
os.system(cmd1)

art_url = """ Artifactory.newServer url: 'http:\/\/%s:%s\/artifactory',"""%(ip_address, art_port) 
cmd2 = """sudo sed -i -e  "s/def server = .*/def server =  %s /"  Test_Gerrit.yaml"""%(art_url)
os.system(cmd2)


jenkinsurl= """http:\/\/%s:%s """%(ip_address , jenkinsport)

print jenkinsurl

if (os.path.isdir('/etc/jenkins_jobs')):
   print "True"
   if (os.path.isfile('/etc/jenkins_jobs/jenkins_jobs.ini')):
     print "exists"
     cmd2 = """sudo sed -i -e  "s/url=.*/url=%s /" /etc/jenkins_jobs/jenkins_jobs.ini"""% (jenkinsurl)
     os.system(cmd2)
   else :
      mk = """sudo touch /etc/jenkins_jobs/jenkins_jobs.ini """
      os.system(mk)
      cp_ini = """ sudo cp jenkins_jobs.ini  /etc/jenkins_jobs/jenkins_jobs.ini """
      os.system(cp_ini)
      cmd2 = """sudo sed -i -e  "s/url=.*/url=%s /" /etc/jenkins_jobs/jenkins_jobs.ini"""% (jenkinsurl)
      os.system(cmd2)
    
else: 
   mk = """sudo mkdir /etc/jenkins_jobs/ """
   os.system(mk)
   mk = """sudo touch /etc/jenkins_jobs/jenkins_jobs.ini """
   os.system(mk)
   cp_ini = """ sudo cp jenkins_jobs.ini  /etc/jenkins_jobs/jenkins_jobs.ini """
   os.system(cp_ini)
   cmd2 = """sudo sed -i -e  "s/url=.*/url=%s /" /etc/jenkins_jobs/jenkins_jobs.ini"""% (jenkinsurl)
   os.system(cmd2)

