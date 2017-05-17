import os,time
from pymongo import MongoClient

def writesuggest(string):
    filePath = '/Users/jdjr/Documents/suggest'
    fileName = 'suggest.txt'
    os.chdir(filePath)
    lines = open(filePath + '/' + fileName,'r').readlines()
    lines.append(string)
    f = open(filePath + '/' + fileName,'w')
    f.writelines(lines)
    f.close()

    return 'done'

def readcontent():
    filePath = '/Users/jdjr/Documents/suggest'
    fileName = 'suggest.txt'
    lines = open(filePath + '/' + fileName,'r').readlines()
    return lines

def writesuggestmongo(string):
    mc = MongoClient("localhost",27017)
    db = mc.suggest
    post_info = db.ceshi

    timeString = gettiemstring()

    post_info.save({'text':string,'time':timeString,'key':'suggest'})

def getsuggestsmongo():
    mc = MongoClient("localhost",27017)
    db = mc.suggest
    post_info = db.ceshi

    dbs = post_info.find({u'key':'suggest'})

    texts = []
    for item in dbs:
        texts.append(dict.get(u'text'))

    return texts

def gettiemstring():
    current = time.localtime(time.time())
    year = current.tm_year
    month = current.tm_mon
    day = current.tm_mday

    yearString = '%i' % year
    monthStrin = '%i' % month
    dayString = '%i' % day

    timeString = yearString + monthStrin + dayString

    return timeString