import os

# os.chdir('/Users/wxg/Documents/JDMobileNew')
os.chdir('/Users/wxg/Documents/JDJRAPPAndroid')

os.system('git checkout -f')

cmd = 'git branch -r'
cmdout = os.popen(cmd)

f = open('/Users/wxg/Desktop/branchesremote.txt','w')
f.write(cmdout.read())
f.close()

cmd1 = 'git branch'
cmdout1 = os.popen(cmd1)

f1 = open('/Users/wxg/Desktop/brancheslocal.txt','w')
f1.write(cmdout1.read())
f1.close()

def getLocalBranchArr():
    f = open('/Users/wxg/Desktop/brancheslocal.txt','r')
    lines = f.readlines()
    return lines

def getRemoteBranchArr():
    f = open('/Users/wxg/Desktop/branchesremote.txt','r')
    lines = f.readlines()
    return lines

linesRemote = getRemoteBranchArr()
linesLoacal = getLocalBranchArr()

remoteCount = len(linesRemote)

for i in range(remoteCount):
    item = linesRemote[i]
    line = item[7:-4]
    line1 = line[7:]
    linesRemote[i] = line1 + '\n'

for i in range(len(linesLoacal)):
    item = linesLoacal[i]
    line = item[2:-4]
    linesLoacal[i] = line + '\n'

hasBranch = False
lineForRemove = []

for itemLocal in linesLoacal:
    for itemRemote in linesRemote:
        if itemLocal == itemRemote:
           hasBranch = True
           break

    if hasBranch == False:
       lineForRemove.append(itemLocal)

    hasBranch = False

f = open('/Users/wxg/Desktop/branchesremove.txt','w')
f.writelines(lineForRemove)
f.close()

f = open('/Users/wxg/Desktop/branchesremote.txt','w')
f.writelines(linesRemote)
f.close()

f1 = open('/Users/wxg/Desktop/brancheslocal.txt','w')
f1.writelines(linesLoacal)
f1.close()


for item in lineForRemove:
    os.system('git branch -D ' + item)


def getBranchArr():
    f = open('/Users/wxg/Desktop/branchesremote.txt','r')
    lines = f.readlines()
    return lines

lines = getBranchArr()

for item in lines:
    gitCheckout = 'git checkout ' + item
    os.system(gitCheckout)
    os.system('git pull')



os.remove('/Users/wxg/Desktop/branchesremove.txt')
os.remove('/Users/wxg/Desktop/branchesremote.txt')
os.remove('/Users/wxg/Desktop/brancheslocal.txt')
