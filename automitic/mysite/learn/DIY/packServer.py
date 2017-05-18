#coding:utf-8
import os,subprocess,sys,shutil
# from mod_pbxproj import XcodeProject
import commands

# def configProject():
#
#     project = XcodeProject.Load('/Users/wxg/Documents/JDMobileNew/JDMobile_2.0/JDMobile.xcodeproj/project.pbxproj')
#
#     for item in project.objects.values():
#         nameIsa = item.get('isa')
#
#         if (nameIsa == 'XCBuildConfiguration'):
#             setting = item.get('buildSettings')
#             nameReference = item.get('baseConfigurationReference')
#             if (nameReference):
#                idStr = setting.get('PRODUCT_BUNDLE_IDENTIFIER')
#                print '---->' + idStr
#                setting.__setitem__('PRODUCT_BUNDLE_IDENTIFIER','com.jd.jinrong2016')
#                setting.__setitem__('PROVISIONING_PROFILE','')
#                setting.__setitem__('PROVISIONING_PROFILE_SPECIFIER','')
#                setting.__setitem__('DEVELOPMENT_TEAM','5TKVHWTT79')
#                setting.__setitem__('CODE_SIGN_IDENTITY[sdk=iphoneos*]','iPhone Developer')
#                item.__setitem__('buildSettings',setting)
#             else:
#                codeSign = setting.get('CODE_SIGN_IDENTITY')
#                profile = setting.get('PROVISIONING_PROFILE')
#                print codeSign
#                print profile
#                # setting.__setitem__('CODE_SIGN_IDENTITY','iPhone Distribution: Beijing Jingdong Century Trading Co., Ltd. (TQZTTUQ9ZE)')
#                # setting.__setitem__('PROVISIONING_PROFILE','0d8cd55a-c922-4f27-b1aa-df6a2f277ea5')
#                setting.__setitem__('CODE_SIGN_IDENTITY','iPhone Developer: 秀刚 王 (F93GC5PGZ9)')
#                setting.__setitem__('PROVISIONING_PROFILE','cb54ac69-0046-4465-869a-7d36b98233f1')
#                item.__setitem__('buildSettings',setting)
#
#         elif (nameIsa == 'PBXProject'):
#             attributes = item.get('attributes')
#             targetAttributes = attributes.get('TargetAttributes')
#             targets = item.get('targets')
#             tar = targets[0]
#             attr = targetAttributes.get('%s' % tar)
#             developmentTeamName = attr.get('DevelopmentTeamName')
#             developmentTeamName = attr.get('ProvisioningStyle')
#             print developmentTeamName
#             attr.__setitem__('DevelopmentTeamName','Beijing Jingdong Century Information Technology Co., Ltd.')
#             attr.__setitem__('ProvisioningStyle', 'Automatic')
#             attr.__setitem__('DevelopmentTeam', '5TKVHWTT79')
#
#     project.save()

def packagiOS(string):

    configProject()
    #os.system('git add .')
    #os.system('git commit -m "config"')

    buildCmd ='xcodebuild -workspace JDFinance.xcworkspace -scheme JDMobile -configuration Debug build'
    f1 = open('/Users/wxg/Desktop/buildlog.txt','r')
    text = f1.read()
    f1.close()

    (status, output) = commands.getstatusoutput(buildCmd)
    f1 = open('/Users/wxg/Desktop/buildlog.txt','w')
    text1 = text + '\n' + output + '%i' % status
    f1.write(text1)
    f1.close()

    targetPath1 = '/Users/wxg/Library/Developer/Xcode/DerivedData/JDFinance-ccfjxqvubpytcfaebakqdwdtjjeu/Build/Products/Debug-iphoneos/JDMobile.app'
    targetPath2 = '/Users/wxg/Documents/Build/iOS/%s/JDMobile.app' % string

    targetPath3 = '/Users/wxg/Documents/Build/iOS/%s' % string

    if (os.path.exists(targetPath3) == False):
         os.mkdir(targetPath3)
         shutil.move('/Users/wxg/Desktop/buildlog.txt',targetPath3+'/buildlog.txt')

    shutil.move(targetPath1, targetPath2)

    if 'BUILD FAILED' in output:
        return 'fail'

    f1 = open(targetPath3+'/buildlog.txt','r')
    text = f1.read()
    f1.close()

    shutil.copyfile('/Users/wxg/Desktop/xrun.py',targetPath3 + '/xrun.py')
    os.chdir(targetPath3)
    (status1, output1) = commands.getstatusoutput('python xrun.py')
    f1 = open(targetPath3+'/buildlog.txt','w')
    text1 = text + '\n' + output1 + '%i' % status1
    f1.write(text1)
    f1.close()
    os.remove('xrun.py')

    returnstring = 'done/iOS/%s' % string
    print returnstring

    return returnstring

def packAndorid(string):

    f1 = open('/Users/wxg/Desktop/buildlog.txt','r')
    text = f1.read()
    f1.close()

    (status, output) = commands.getstatusoutput('gradle assembleDebug')
    f1 = open('/Users/wxg/Desktop/buildlog.txt','w')
    text1 = text + '\n' + output + '%i' % status
    f1.write(text1)
    f1.close()

    path = '/Users/wxg/Documents/Build/Android'
    if (os.path.exists(path) == False):
        os.mkdir(path)

    path1 = '/Users/wxg/Documents/Build/Android/{}'.format(string)

    if (os.path.exists(path1) == False):
        os.mkdir(path1)
        shutil.move('/Users/wxg/Desktop/buildlog.txt',path1+'/buildlog.txt')

    if 'BUILD FAILED' in output:
        return 'failed'

    pathDebug = '/Users/wxg/Documents/JDJRAPPAndroid/JDJR/build/outputs/apk/JDJR-debug-unaligned.apk'
    pathDebugT = '/Users/wxg/Documents/Build/Android/{}/JDJR-debug-unaligned.apk'.format(string)

    if (os.path.exists(pathDebug) == True):
        if (os.path.exists(pathDebugT) == True):
            os.remove(pathDebugT)
        shutil.copyfile(pathDebug, pathDebugT)

    pathDebug1 = '/Users/wxg/Documents/JDJRAPPAndroid/JDJR/build/outputs/apk/JDJR-debug.apk'
    pathDebugT1 = '/Users/wxg/Documents/Build/Android/{}/JDJR-debug.apk'.format(string)

    if (os.path.exists(pathDebug1) == True):
        if (os.path.exists(pathDebugT1) == True):
            os.remove(pathDebugT1)
        shutil.copyfile(pathDebug1,pathDebugT1)

    pathRelease = '/Users/wxg/Documents/JDJRAPPAndroid/JDJR/build/outputs/apk/JDJR-release-unsigned.apk'
    pathReleaseT = '/Users/wxg/Documents/Build/Android/{}/JDJR-release-unsigned.apk'.format(string)

    if (os.path.exists(pathRelease) == True):
       if (os.path.exists(pathReleaseT) == True):
          os.remove(pathReleaseT)
       shutil.copyfile(pathRelease,pathReleaseT)

    # returnstring = pathDebugT1 + 'done'
    # print pathDebugT1
    # print 'ceshi'
    return 'Android/' + string + 'done'

def getbranchesI(string):
    os.chdir('/Users/wxg/Documents/JDMobileNew')
    os.popen('git fetch')
    cmdline = 'git branch -r'
    cmdout = os.popen(cmdline)
    #f = open('/Users/wxg/Desktop/branches.txt','r')
    #textlist = f.read()
    #os.remove('/Users/wxg/Desktop/branches.txt')
    return cmdout.read()

def getbranchesA(string):
    os.chdir('/Users/jdjr/Git/JDJRAPPAndroid')
    os.popen('git fetch')
    cmd = 'git branch -r'
    cmdout = os.popen(cmd)
    return cmdout.read()

def changeToOnlineI():
    lines=open("/Users/wxg/Documents/JDMobileNew/JRLibrary/JRMacro/ConfigManager.h",'r').readlines()
    flen=len(lines)-1
    for i in range(20):
       if '#define' in lines[i]:
           if '//' not in lines[i]:
              lines[i] = '//' + lines[i]

    open("/Users/wxg/Documents/JDMobileNew/JRLibrary/JRMacro/ConfigManager.h",'w').writelines(lines)

def changeToOfflineI():
    lines=open("/Users/wxg/Documents/JDMobileNew/JRLibrary/JRMacro/ConfigManager.h",'r').readlines()
    flen=len(lines)-1
    for i in range(20):
        if '#define' in lines[i]:
            if '//' not in lines[i]:
                lines[i] = '//' + lines[i]

            if '//#define JDJR_NetWork_Beta' in lines[i]:
                lines[i] = lines[i].replace('//','')

    open("/Users/wxg/Documents/JDMobileNew/JRLibrary/JRMacro/ConfigManager.h",'w').writelines(lines)

