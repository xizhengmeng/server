import os
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

    mc = MongoClient("localhost",27017)

    db = mc.users

    return 'done'

def readcontent():
    filePath = '/Users/jdjr/Documents/suggest'
    fileName = 'suggest.txt'
    lines = open(filePath + '/' + fileName,'r').readlines()
    return lines
