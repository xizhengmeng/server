import os

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
