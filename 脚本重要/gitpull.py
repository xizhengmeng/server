import os

f = open('/Users/wxg/Desktop/branchName.txt','r')
branchName = f.read()
branchName = branchName.replace('origin ','')
branchName = branchName.replace('origin/','')
branchName = branchName.strip()
f.close()
print branchName

cmd = 'git checkout %s' % branchName
cmdout = os.popen(cmd)
text1 = cmdout.read()

cmd1 = 'git pull origin %s' % branchName
cmd1out = os.popen(cmd1)
text2 = cmd1out.read()

f = open('/Users/wxg/Desktop/gitlog.txt','w')
f.write(branchName + text1 + text2)
f.close()
