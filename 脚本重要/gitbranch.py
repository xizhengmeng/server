import os

cmd = 'git branch -r'
cmdout = os.popen(cmd)

f = open('/Users/wxg/Desktop/branches.txt','w')
f.write(cmdout.read())
f.close()
