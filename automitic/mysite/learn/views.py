#coding:utf-8
import os,datetime
from django.http import HttpResponse
from django.shortcuts import render
from DIY.compute import getModelFromJson
from DIY.createui import getCreatedStringWithProperties
from django.http import HttpResponseRedirect
from DIY.mail import sendMail
from DIY.packServer import getbranchesA,packAndorid
from DIY.APIServer import getfilecontent,writecontent,checkfile,createfolder
from DIY.Suggest import writesuggest,readcontent,writesuggestmongo,getsuggestsmongo
import shutil
import logging
import commands,time
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

#def some_view(request):
    #...

#logger = logging.getLogger(__name__)

def home(request):
    string = '这是'
    return render(request,'home.html',{'string':string})

def nextPage(request):
    return render(request,'next.html')

def compute(request):
    string = request.GET['text']
    string = getModelFromJson(string)
    return HttpResponse(string)

def uicreate(request):
    return render(request,'UICreate.html')

def suggest(request):
    return render(request,'Suggest.html')

def packAndroid(request):
    return render(request,'package.html')

def webserver(request):
    return render(request,'WebServer.html')

def webserverfullre(request):
    return render(request,'WebServerFull.html')

def createui(request):
    string = request.GET['text']
    string = getCreatedStringWithProperties(string)
    return HttpResponse(string)

def pullBranch(dir):
    path = '/Users/jdjr/Desktop/branches.txt'
    f1 = open(path,'w')
    f1.write(dir)
    f1.close()

    unsuccess = True

    while unsuccess:
          f1 = open(path,'r')
          text = f1.read()
          if len(text) == 0:
              unsuccess = False

          f1.close()

def mvoeTargetFile(string):

    filePathF = '/Users/jdjr/Documents/upload/'
    fileList = os.listdir(filePathF)

    filePath = '/Users/jdjr/Documents/JDJRAPPAndroid/JDJR/libs/'
    filePathN = filePath + 'armeabi/'

    f = open('/Users/jdjr/Documents/Build/uploadlog.txt','a')

    for fileName in fileList:
        f.write(fileName + '\n')
        targetPath = filePath + fileName
        targetPathN = filePathN + fileName

        filePahtEnd = ''
        if os.path.exists(targetPath):
           filePahtEnd = filePath
        elif os.path.exists(targetPathN):
           filePahtEnd = filePathN
        else:
           print 'file is not exists'

        shutil.move(filePathF + fileName,filePahtEnd + fileName)

    begin = datetime.datetime.now()
    hour = begin.hour + 8
    day = begin.day
    if hour > 24:
       hour = hour - 24
       day = day + 1

    timeStr = '%dM%.dD%.dH%.dM' % (begin.month, day, hour,begin.minute)
    f.write(string +'***'+ timeStr + '\n\n')
    f.close()

def ajaxgetbranchesfuncI(request):
    return HttpResponse(getbranchesI('string'))

def ajaxgetbranchesfuncA(request):
    return HttpResponse(getbranchesA('string'))

def buildlist(requets):
    return HttpResponseRedirect('http://10.13.80.73:8000/Documents/Build')

def sendMails(request):
    print 'mail'
    sendMail('')
    return HttpResponse('hi')  

def jsonFormat1(request):
    return HttpResponseRedirect('http://www.jsonparseronline.com')

def jsonFormat2(request):
    return HttpResponseRedirect('http://www.bejson.com')    

def interfaceTest(request):
    return HttpResponseRedirect('http://www.atool.org/httptest.php')

def blockClickview(request):
    return HttpResponseRedirect('http://www.hanson647.com')    

def upload_file(request):

    if request.method == "POST":
        myFile1 =request.FILES.get("myfile1", None)
        myFile2 =request.FILES.get("myfile2", None)

        filePathTemp = '/Users/jdjr/Documents/upload/'
        filePath = '/Users/jdjr/Documents/JDJRAPPAndroid/JDJR/libs/'
        filePathN = filePath + 'armeabi/'

        if myFile1:
           targetPath = filePath + myFile1.name
           targetPathN = filePathN + myFile1.name

           filePahtEnd = ''
           if os.path.exists(targetPath):
               filePahtEnd = filePath
           elif os.path.exists(targetPathN):
               filePahtEnd = filePathN
           else:
               return HttpResponse('fail-----%s is not exist' % myFile1.name)

           destination = open(os.path.join(filePahtEnd, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

           destination1 = open(os.path.join(filePathTemp, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination1.write(chunk)
           destination1.close()

        if myFile2:
           targetPath = filePath + myFile2.name
           targetPathN = filePathN + myFile2.name

           filePahtEnd = ''
           if os.path.exists(targetPath):
              filePahtEnd = filePath
           elif os.path.exists(targetPathN):
               filePahtEnd = filePathN
           else:
               return HttpResponse('fail-----%s is not exist' % myFile2.name)

           destination = open(os.path.join(filePahtEnd, myFile2.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

           destination1 = open(os.path.join(filePathTemp, myFile2.name),'wb+')
           for chunk in myFile2.chunks():
               destination1.write(chunk)
           destination1.close()

        #filelistStr = ''
        #count = 0
        #for filename in os.listdir(filePath):
            #if filename[0] != '.':
               #count = count + 1
               #filename = '(%.0f)'  % count + filename + '_____'
               #filelistStr += filename

        #return HttpResponse('upload over!' + 'dir list:' + filelistStr)
        os.chdir('/Users/jdjr/Documents/JDJRAPPAndroid')
        text = os.popen('git status')
        textStr = text.read()

        return HttpResponse('success' +'<br>'+ textStr)

def upload_urls_file(request):
    if request.method == "POST":
        text = request.POST.get('inputId')
        if (text):
            print text
        else:
            return HttpResponse('失败---------请输入接口标识')

        myFile1 =request.FILES.get("myfile1", None)
        myFile2 =request.FILES.get("myfile2", None)
        myFile3 =request.FILES.get("myfile3", None)
        myFile4 =request.FILES.get("myfile4", None)
        myFile5 =request.FILES.get("myfile5", None)
        myFile6 =request.FILES.get("myfile6", None)
        myFile7 =request.FILES.get("myfile7", None)

        filePath = '/Users/jdjr/Documents/APIServer/' + text

        if (not os.path.exists(filePath)):
            os.mkdir(filePath)

        if myFile1:
           destination = open(os.path.join(filePath, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

        if myFile2:
           destination = open(os.path.join(filePath, myFile2.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile3:
           destination = open(os.path.join(filePath, myFile3.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile4:
           destination = open(os.path.join(filePath, myFile4.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile5:
           destination = open(os.path.join(filePath, myFile5.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile6:
           destination = open(os.path.join(filePath, myFile6.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile7:
           destination = open(os.path.join(filePath, myFile7.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        filelistStr = ''
        count = 0
        for filename in os.listdir(filePath):
            if filename[0] != '.':
               count = count + 1
               filename = '(%.0f)'  % count + filename + '<br/>'
               filelistStr += filename

        return HttpResponse(text + '<br/>' + 'upload over!<br/>' + 'dir list:<br/>' + filelistStr)

def ajaxpackapp(request):
    time1 = time.time()
    f = open('/Users/jdjr/Documents/Build/building.txt','r')
    text = f.read()

    if (text != ''):
        return HttpResponse('wait')

    branchName = request.GET['branch']
    index = branchName.index('/')
    branchName = branchName[index + 1:]

    platName = request.GET['platName']
    # folderName = request.GET['folderName']
    textOnline = request.GET['textOnline']

    f1 = open('/Users/jdjr/Desktop/buildlog.txt','w')

    f1.write(branchName + '\n')
    f1.write(platName + '\n')
    # f1.write(folderName + '\n')
    f1.write(textOnline + '\n')
    f1.close()

    if text == '':
       if (platName == 'Andorid'):

           f1 = open('/Users/jdjr/Documents/Build/building.txt','w')
           f1.write('Andorid' + branchName)
           f1.close()

           os.chdir('/Users/jdjr/Documents/JDJRAPPAndroid')

           os.system('git checkout -f')

           cmd = 'git checkout %s' % branchName
           #os.system(cmd)
           (status, output) = commands.getstatusoutput(cmd)
           f1 = open('/Users/jdjr/Desktop/buildlog.txt','r')
           text = f1.read()
           f1.close()

           f1 = open('/Users/jdjr/Desktop/buildlog.txt','w')
           text1 = text + '\n' + output + '%i' % status
           f1.write(text1)
           f1.close()

           mvoeTargetFile(branchName)

           pullBranch('/Users/jdjr/Documents/JDJRAPPAndroid' + '\n' + branchName)

           begin = datetime.datetime.now()
           hour = begin.hour + 8
           day = begin.day
           if hour > 24:
              hour = hour - 24
              day = day + 1

           timeStr = '%dM%.dD%.dH%.dM' % (begin.month, day, hour,begin.minute)

           text = packAndorid(branchName + '**' + textOnline + '**' + timeStr)

           f2 = open('/Users/jdjr/Documents/Build/building.txt','w')
           f2.write('')
           f2.close()

           os.chdir('/Users/jdjr/Documents/JDJRAPPAndroid')
           (status, output) = commands.getstatusoutput('git add .')
           (status1, output1) = commands.getstatusoutput('git checkout -f')

           time2 = time.time() - time1
           timeE = round(time2,1)

           pathN = '/Users/jdjr/Documents/Build/buildlog.txt'
           string = branchName + ' ' + textOnline + ' ' + platName  + ' ' + timeStr + ' ' + 'totalTime:' + '%.0f' % timeE
           if os.path.exists(pathN):
              f = open(pathN,'r')
              text = f.read()
              f.close()
              f = open(pathN,'w')
              f.write(text + '\n' + string)
              f.close()

           print text + 'cehsiaceshi'
           if text == 'failed':
              return HttpResponse('fail')

           return HttpResponse('done')
       else:

           f1 = open('/Users/jdjr/Documents/Build/building.txt','w')
           f1.write('iOS' + branchName)
           f1.close()

           os.chdir('/Users/jdjr/Documents/JDMobileNew')

           (status, output) = commands.getstatusoutput('git add .')
           (status1, output1) = commands.getstatusoutput('git checkout -f')

           cmd = 'git checkout {}'.format(branchName)

           (status3, output3) = commands.getstatusoutput(cmd)
           f1 = open('/Users/jdjr/Desktop/buildlog.txt','r')
           text = f1.read()
           f1.close()

           f1 = open('/Users/jdjr/Desktop/buildlog.txt','w')
           text1 = text + '\n' + output + '%i' % status + '\n' + output3 + '%i' % status3
           f1.write(text1)
           f1.close()

           pullBranch('/Users/jdjr/Documents/JDMobileNew' + '\n' + branchName)

           if (textOnline == 'online'):
              changeToOnlineI()
           else:
              changeToOfflineI()

           begin = datetime.datetime.now()
           hour = begin.hour + 8
           day = begin.day
           if hour > 24:
              hour = hour - 24
              day = day + 1

           timeStr = '%dM%.dD%.dH%.dM' % (begin.month, day, hour,begin.minute)

           text = packagiOS(branchName + '**' + textOnline  + '**' +timeStr)

           f2 = open('/Users/jdjr/Documents/Build/building.txt','w')
           f2.write('')
           f2.close()

           if text == 'fail':

              time2 = time.time() - time1
              timeE = round(time2,1)
              pathN = '/Users/jdjr/Documents/Build/buildlog.txt'
              string = branchName + ' ' + textOnline + ' ' + platName + ' ' + timeStr + ' ' + 'totalTime:' + '%.0f' % timeE + ' '+ 'build failed'
              if os.path.exists(pathN):
                 f = open(pathN,'r')
                 text = f.read()
                 f.close()
                 f = open(pathN,'w')
                 f.write(text + '\n' + string)
                 f.close()

              os.chdir('/Users/jdjr/Documents/JDMobileNew')
              os.system('git add .')
              os.system('gie checkout -f')
              shutil.rmtree('/Users/jdjr/Library/Developer/Xcode/DerivedData/JDFinance-ccfjxqvubpytcfaebakqdwdtjjeu')
              return HttpResponse('fail')

           os.chdir('/Users/jdjr/Documents/JDMobileNew')
           (status, output) = commands.getstatusoutput('git add .')
           (status1, output1) = commands.getstatusoutput('git checkout -f')

           time2 = time.time() - time1
           timeE = round(time2,1)

           pathN = '/Users/jdjr/Documents/Build/buildlog.txt'
           string = branchName + ' ' + textOnline + ' ' + platName + ' ' + timeStr + ' ' + 'totalTime:' + '%.0f' % timeE + ' '+'build success'
           if os.path.exists(pathN):
              f = open(pathN,'r')
              text = f.read()
              f.close()
              f = open(pathN,'w')
              f.write(text + '\n' + string)
              f.close()

           return HttpResponse('done')

def getUrl1(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text1.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text1.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl2(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text2.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text2.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl3(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text3.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text3.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl4(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text4.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text4.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl5(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text5.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text5.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl6(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text6.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text6.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl7(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/jdjr/Documents/APIServer/' + text + '/text7.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text.txt not exist' % text)
    else:
        return HttpResponse('please give an name')


def getcontentstring(request):
    filename = request.GET.get('filename')
    text = getfilecontent(filename)
    return HttpResponse(text)


def writestring(request):
    content = request.POST.get('content')
    foldername = request.POST.get('foldername')
    filename = request.POST.get('filename')
    answer = writecontent(content,foldername,filename)
    return HttpResponse(answer)


def checkfilelist(request):
    name = request.GET.get('foldername')
    text = checkfile(name)
    return HttpResponse(text)

def createforder(request):
    foldername = request.GET.get('foldername')
    text = createfolder(foldername)
    return HttpResponse(text)

def downloadipafunction(request):
    url = request.GET.get('url')
    return HttpResponseRedirect(url)

def indexPage(request):
    return render(request,'checkIndex.html')

def getindexall(request):
    content = request.POST.get('name')
    listAll = getindex(content)
    # listNew = []
    # for item in listAll:
    #     listNew.append(str(item))
    # liststring = ''.join(listNew)
    # liststring = liststring.encode('utf-8')
    return HttpResponse(listAll)

def getindexrank(request):
    getindexrankfun()
    return HttpResponse()

def gotojinkens(request):
    return HttpResponseRedirect('http://bds.cbpmgt.com/jenkins/job/ios_jdjr/')

def gotogitjdjr(request):
    return HttpResponseRedirect('http://jcode.cbpmgt.com')

def insertsuggest(request):
    text = request.POST.get('content')
    print text
    answer = writesuggestmongo(text)
    print answer
    return HttpResponse('done')

def gotobugly(request):
    return HttpResponseRedirect('https://bugly.qq.com/v2/workbench/apps')

def gotoredmine(request):
    return HttpResponseRedirect('http://pm.jdfin.local/redmine/')

def readcontentview(request):
    lines = getsuggestsmongo()
    return HttpResponse(lines)