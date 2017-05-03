import os,commands,shutil

#os.chdir('/Users/wxg/Documents/JDMobile')
path = '/Users/wxg/Desktop/branches.txt'

while True:
    if os.path.exists(path):
       f1 = open(path,'r')
       dir = f1.read()
       f1.close()
       if len(dir) > 0:
          print dir
          
          os.chdir(dir)
          
          (status, output) = commands.getstatusoutput('git pull')

          f1 = open('/Users/wxg/Desktop/buildlog.txt','r')
          text = f1.read()
          f1.close()

          f1 = open('/Users/wxg/Desktop/buildlog.txt','w')
          text1 = text + '\n' + output + '%i' % status
          f1.write(text1)
          f1.close()

          f2 = open(path,'w')
          f2.write('')
          f2.close()




