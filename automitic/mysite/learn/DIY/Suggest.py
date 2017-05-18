import os,time,json
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
        dic = {}
        dic['text'] = item.get(u'text')
        dic['time'] = item.get(u'time')
        texts.append(dic)

    datas = json.dumps(texts)

    return datas

def gettiemstring():
    current = time.localtime(time.time())
    year = current.tm_year
    month = current.tm_mon
    day = current.tm_mday
    hour = current.tm_hour
    min  = current.tm_min
    sec = current.tm_sec

    hour = hour + 8
    if (hour > 24):
        hour = hour - 24
        day = day + 1

    yearString = '%i' % year
    monthStrin = '%i' % month
    dayString = '%i' % day
    hourStr = '%i' % hour
    minStr = '%i' % min
    secStr = '%i' % sec

    timeString = yearString + '/'+ monthStrin +'/'+  dayString  + '   '+ hourStr + ':'+ minStr

    return timeString