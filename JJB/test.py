import fileinput, re, os
filename = 'Test_Gerrit_Trigger.txt'

name = "Demo"

server="server-name: " + name 
with fileinput.FileInput(filename, inplace=True, backup='.bak') as file:
    for line in file:
        print(re.sub("server-name:/s", server, line), end = '')


#with open(FileName) as f:
# newText=f.read().replace('Demo_Gerrit1_new_test', 'Oranges')
 
#with open(FileName, "w") as f:
# f.write(newText)
