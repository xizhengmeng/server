import os,subprocess,shutil,json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getfilecontent(filename):
    filePath = '/Users/wxg/Documents/APIServer'
    filelist = filename.split('+')
    foldername = filelist[0]
    filename = filelist[1]
    filename = 'text' + filename[3:] + '.txt'
    finalFilePath = filePath + '/' + foldername + '/' + filename
    f = open(finalFilePath,'r')
    text = f.read()
    f.close()
    return text

def writecontent(string,foldername,filename):
    data = json.loads(string)
    filename = 'text' + filename[3:] + '.txt'
    filePath = '/Users/jdjr/Documents/APIServer'
    finalFilePath = filePath + '/' + foldername + '/' + filename
    if data:
       f = open(finalFilePath,'w')
       f.write(string)
       f.close()
       return 'done'
    else:
       return 'error for json'

def checkfile(string):
    filePath = '/Users/jdjr/Documents/APIServer/'
    finalfilePath = filePath + string

    if (os.path.exists(finalfilePath) == False):
       createfolder(string)

    filelist = os.listdir(finalfilePath)
    string = ''
    for item in filelist:
        if item[0] != '.':
           string = string + item + '+'

    return string

def createfolder(string):
    filePath = '/Users/jdjr/Documents/APIServer/'
    finalFilePath = filePath + string

    if os.path.exists(finalFilePath) == True:
       return 'file exists'

    os.mkdir(finalFilePath)

    os.chdir(finalFilePath)

    for i in range(1,10):
        filename = 'text%i.txt' % i
        finalFilePathName = finalFilePath + '/' + filename
        f = open(finalFilePathName,'w')
        f.close()

    return 'done'