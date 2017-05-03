import os

# os.chdir('/Users/wxg/Documents/JDMobileNew')
os.chdir('/Users/wxg/Documents/JDJRAPPAndroid')
cmd1 = 'git branch'
cmdout1 = os.popen(cmd1)

f1 = open('/Users/wxg/Desktop/brancheslocal.txt','w')
f1.write(cmdout1.read())
f1.close()

def getLocalBranchArr():
    f = open('/Users/wxg/Desktop/brancheslocal.txt','r')
    lines = f.readlines()
    return lines

linesLoacal = getLocalBranchArr()

for i in range(len(linesLoacal)):
    item = linesLoacal[i]
    line = item[2:-4]
    linesLoacal[i] = line + '\n'

hasBranch = False
lineForRemove = []

for item in linesLoacal:
    os.system('git branch -D ' + item)

