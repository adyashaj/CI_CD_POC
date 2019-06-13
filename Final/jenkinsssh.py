
import fileinput, re, os,time



def getVarFromFile(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()


getVarFromFile('variable.txt')

jenkinsContainer=data.jenkinsContainerid
jenkinsHostName=data.jenkinsHostName


path = os.getcwd()
os.chdir(path)

print path 



rm = """sudo rm -rf .ssh"""
os.system(rm)

dir = """sudo mkdir .ssh""" 
os.system(dir)



path3 = ".ssh/id_rsa"
path4 = (os.path.join(path, path3))
print path4


ssh ="""sudo ssh-keygen -f %s  -C jenkins@%s -N  '' """% (path4 , jenkinsContainer)
os.system(ssh)


path1 = ".ssh"
path2 = (os.path.join(path, path1))
print path2

#Changing Directory

os.chdir(path2)

 
id = """sudo chown jenkins:jenkins id_rsa"""
os.system(id)


id_pub = """sudo chown jenkins:jenkins id_rsa.pub"""
os.system(id_pub)

chmod = """sudo chmod 777 id_rsa"""
os.system(chmod)

chmod1 = """sudo chmod 777 id_rsa.pub"""
os.system(chmod1)

copy_ssh = """sudo docker cp %s  %s:/var/jenkins_home"""%(path2 , jenkinsHostName)
os.system(copy_ssh)

restart = """docker restart %s"""%(jenkinsHostName)
os.system(restart)

rm = """sudo rm -rf .ssh"""
os.system(rm)


time.sleep(30)
