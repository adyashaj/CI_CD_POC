import fileinput, re, os,time



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

#openurl =""" xdg-open "http://%s:%s/" """%(ip_address , port_number)
#os.system(openurl)

time.sleep(10)


user_creation = """ curl -X PUT -H 'Content-Type: application/json'  -u '%s:%s' -i 'http://%s:%s/a/accounts/%s' --data '{
    "name": '%s',
    "email": '%s',
    "http_password": '%s',
    "groups": [
      "Non-Interactive Users",
      "Administrators"
    ]
  }' """% (username , password ,  ip_address , port_number , gJUser , gJUser , gJUEmail , gJCredentials)



result = os.popen(user_creation).read()

print result

change= re.search('"_account_id":(.+?),',result)
account_id = change.group(1).strip()
print account_id

# Get current Working Directory

path = os.getcwd()
os.chdir(path)


cp_ssh = ("""sudo docker cp  %s:/var/jenkins_home/.ssh/id_rsa.pub %s""")% (jenkinsName,path)

os.system(cp_ssh)


idpath = "id_rsa.pub"
idpub = (os.path.join(path, idpath))
print idpub


file=open(idpub,'rt')
str = ""
lines=str.join(file.readlines())

key =lines.strip()

print key


ssh_key = """curl -X POST  -H 'Content-Type: plain/text'   -u '%s:%s' -i 'http://%s:%s/a/accounts/%s/sshkeys' --data '%s' """%(username , password , ip_address , port_number, account_id , key)

os.system(ssh_key)


id_pub_rm = """sudo rm -rf id_rsa.pub"""
os.system(id_pub_rm)

# initializing Git repository
   
cmd1 ="sudo git init" 
os.system(cmd1)

gituser = """sudo git config --global user.name "admin" """
os.system(gituser)



gituserEmail= " sudo git config --global user.email admin@example.com"
os.system(gituserEmail)


# Setting Remote Origin

set_origin = " sudo git remote add  origin http://%s@%s:%s/a/All-Projects"% (username ,ip_address , port_number)
os.system(set_origin)


# Cloning Remote repo

clone = """git clone http://%s:%s@%s:%s/a/All-Projects && (cd All-Projects && curl -kLo `git rev-parse --git-dir`/hooks/commit-msg http://%s:%s@%s:%s/tools/hooks/commit-msg; chmod +x `git rev-parse --git-dir`/hooks/commit-msg)"""% (username , password , ip_address , port_number , username ,password, ip_address , port_number) 

os.system(clone) # Cloning

# Joining All-Projects to current working directory

path1 = "All-Projects"
path2 = (os.path.join(path, path1))
#print path2

# Changing Directory

os.chdir(path2)

# Removing Project.config file

cmd2 = "sudo rm -rf project.config"
os.system(cmd2)


# Creating New File

cmd3 = "sudo touch project.config"
os.system(cmd3)


# Storing Project.config in Text Variable

text = """[project]
	description = Access inherited by all other projects.
[receive]
	requireContributorAgreement = false
	requireSignedOffBy = false
	requireChangeId = true
	enableSignedPush = true
	createNewChangeForAllNotInTarget = false
	rejectImplicitMerges = false 
[submit]
	mergeContent = true
	action = merge always
[capability]
	administrateServer = group Administrators
	administrateServer = group Project Owners
	priority = batch group Non-Interactive Users
	priority = batch group Project Owners
	streamEvents = group Non-Interactive Users
	streamEvents = group Project Owners
[access "refs/*"]
	read = group Administrators
	read = group Anonymous Users
	read = group Non-Interactive Users
	push = +force group Administrators
	push = group Project Owners
	submit = group Administrators
	submit = group Project Owners
[access "refs/for/*"]
	addPatchSet = group Registered Users
	push = group Administrators
	push = group Project Owners
	submit = group Administrators
	submit = group Project Owners
[access "refs/for/refs/*"]
	push = group Administrators
	push = group Registered Users
	pushMerge = group Administrators
	pushMerge = group Registered Users
[access "refs/heads/*"]
	create = group Administrators
	create = group Project Owners
	forgeAuthor = group Registered Users
	forgeCommitter = group Administrators
	forgeCommitter = group Project Owners
	push = +force group Administrators
	push = +force group Project Owners
	label-Code-Review = -2..+2 group Administrators
	label-Code-Review = -2..+2 group Project Owners
	label-Code-Review = -1..+1 group Registered Users
	submit = group Administrators
	submit = group Project Owners
	editTopicName = +force group Administrators
	editTopicName = +force group Project Owners
	pushMerge = group Administrators
	label-Verified = -1..+1 group Non-Interactive Users
[access "refs/meta/config"]
	exclusiveGroupPermissions = active
	active = group Administrators
	active = group Project Owners
	active = group Non-Interactive Users
	create = group Administrators
	create = group Project Owners
	push = +force group Administrators
	push = +force group Project Owners
	label-Code-Review = -2..+2 group Administrators
	label-Code-Review = -2..+2 group Project Owners
	submit = group Administrators
	submit = group Project Owners
	pushMerge = group Administrators
	pushMerge = group Project Owners
	owner = group Administrators
        owner = group Project Owners
[access "refs/tags/*"]
	create = group Administrators
	create = group Project Owners
	createTag = group Administrators
	createTag = group Project Owners
	createSignedTag = group Administrators
	createSignedTag = group Project Owners
[label "Code-Review"]
	function = MaxWithBlock
	defaultValue = 0
	copyMinScore = true
	copyAllScoresOnTrivialRebase = true
	value = -2 This shall not be merged
	value = -1 I would prefer this is not merged as is
	value =  0 No score
	value = +1 Looks good to me, but someone else must approve
	value = +2 Looks good to me, approved
[plugin "uploadvalidator"]
	blockedContentTypeWhitelist = false
	maxPathLength = 0
	rejectDuplicatePathnames = false
	rejectDuplicatePathnamesLocale = en
	rejectSubmodule = false
	rejectSymlink = false
	rejectWindowsLineEndings = false
[label "Verified"]
	function = MaxWithBlock
	value = -1 Failed
	value =  0 No score
	value = +1 Verified
	defaultValue = 0"""
f = open('project.txt','w+')
f.write(text)
f.close()

# Moving project.txt to Project.config

cmd4 = "sudo mv project.txt project.config"
os.system(cmd4)

# Adding changes to staging area

cmd5 =  "git add ."
os.system(cmd5)

# Commit changes made

cmd6 =   "git commit  -a -m 'Edited project config' "
os.system(cmd6)

# Pushing Changes back to repo

cmd7 = "git push  origin HEAD:refs/for/refs/meta/config"
os.system(cmd7)

os.chdir(path)
remove = "sudo rm -rf All-Projects"
os.system(remove)



#Getting Change_id

get_changeid = """curl -X GET -H 'Content-Type: application/json' -u '%s:%s' -i 'http://%s:%s/a/changes/?q=is:open+owner:self&q=is:open+reviewer:self+-owner:self&q=is:closed+owner:self+limit:5&o=LABELS' """% (username , password , ip_address , port_number )

result = os.popen(get_changeid).read()

print result


change = re.search('"change_id":(.+?),',result)
changeid = change.group(1).strip().replace('"', '')
print changeid

#code_review


code_review = """ curl -X POST -H 'Content-Type: application/json'  -u '%s:%s' -i 'http://%s:%s/a/changes/%s/revisions/current/review' --data '{
    "tag": "Sindhu",
    "message": "All Good",
    "labels": {
      "Code-Review": +2
   }
}
' """% (username , password ,  ip_address , port_number, changeid )

os.system(code_review)


# Submit and Merge

submit = """ curl -X POST -H 'Content-Type: application/json'  -u '%s:%s'  -i 'http://%s:%s/a/changes/%s/submit' --data '{
    "admin": 1000000
  }' """% (username , password ,  ip_address , port_number, changeid )

os.system(submit)


#gituser = """sudo git config --global user.name "Jenkins" """
#os.system(gituser)

#gituserEmail= " sudo git config --global user.email jenkins@example.com"
#os.system(gituserEmail)

#username=data.gerritUserName
#password=data.gerritCredentials
#ip_address=data.gerritHostName
#port_number=data.gerritHttpPort

# Creating_Gerrit_Project



#create_project = """curl -X PUT -H 'Content-Type: application/json' -u '%s:%s'  -i 'http://%s:%s/a/projects/Gerrit_Trigger' --data ' {
#    "description": "This is a demo project.",
#    "submit_type": "CHERRY_PICK",
#    "owners": [
#      "Administrators",
#     "Non-Interactive Users"
#         ]
#  }'"""% (username , password , ip_address , port_number )

#result = os.popen(create_project).read()

#print result

# Restart_Gerrit


restart_docker = "docker restart %s"% (gerrit_container_name)

os.system (restart_docker)

