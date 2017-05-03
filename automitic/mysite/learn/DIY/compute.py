#utf-8

import json

class types:
    string = 0
    integer = 1
    bool = 2
    list = 3
    dict = 4

endString = ''
dictList = []
impList = []
arrNameList = []

def getModelFromJson(string):
    global endString
    dict = json.loads(string)
    endString += handleDic(dict,'')
    handleDicList()

    returnString = endString
    endString = ''

    returnString += '\n-----------------------------implemention-----------------------------\n'
    for impstring in impList:
        returnString += impstring

    del  impList[:]

    return returnString

def handleDicList():
    if (len(dictList) == 0):
        return

    global endString
    value = dictList[0]
    if (type(value) == type({})):
        classNameString = ''
        if 'className' in value.keys():
            classNameString = value['className']
            value.pop('className')
        endString += '\n%s' % handleDic(value,classNameString)
    elif (type(value) == type([])):
        endString += '\n%s' % handleList(value)
    else:
        pass
    dictList.remove(value)
    handleDicList()

def handleDic(dict, className):

    global arrNameList
    global impList
    global dictList
    typev = 0
    returnstring = ''

    for key in dict:
        value = dict[key]
        if type(value) == type(u'name'):
            typev = 0
        elif type(value) == type('name'):
            typev = 0
        elif type(value) == type(1):
            typev = 1
        elif type(value) == type(True):
            typev = 2
        elif type(value) == type([]):
            typev = 3
            if (type(value[0]) == type({})):
                value[0]['className'] = key
                arrNameList.append(key)
            dictList.append(value)
        elif type(value) == type({}):
            typev = 4
            value['className'] = key
            dictList.append(value)
        returnstring += '%s;\n' % getFullNameWithNameAndType(key, typev)

    if className:
       impList.append(handlImpWithClassNameAndArrNameList(className, arrNameList))
       return '\n@interface %sModel : NSObject\n%s@end' % (className.capitalize(),returnstring)
    else:
       impList.append(handlImpWithClassNameAndArrNameList('<#ModelName#>', arrNameList))
       return '\n@interface <#ModelName#> : NSObject\n%s@end' % returnstring

def handleList(list):
    value = list[0]

    if (type(value) == type({})):
        classNameString = ''
        if 'className' in value.keys():
            classNameString = value['className']
            value.pop('className')
        else:
            pass
        string = handleDic(value, classNameString)
        if len(string) > 0:
           return string
        else:
          return ''
    else:
        return ''

def getFullNameWithNameAndType(name, type):

    if type == types.string:
       return '@property (nonatomic, strong) NSString *%s' % name
    elif type == types.integer:
       return '@property (nonatomic, assign) NSInteger %s' % name
    elif type == types.bool:
       return '@property (nonatomic, assign) BOOL %s' % name
    elif type == types.list:
       return '@property (nonatomic, strong) NSArray *%s' % name
    elif type == types.dict:
       return '@property (nonatomic, strong) %sModel *%s' % (name.capitalize(),name)
    else:
       return 'none'


def handlImpWithClassNameAndArrNameList(className, arrNameList):
    impString = ''
    if className == u'<#ModelName#>':
        impString += '\n@implementation %s\n' % className
    else:
        impString += '\n@implementation %sModel\n' % className.capitalize()

    dictString = ''
    for key in arrNameList:
        dictString += '@"%s" : [%sModel class],\n' % (key, key.capitalize())

    if len(dictString) > 0:
       impString += '+ (NSDictionary *)objectClassInArray {\n    return @{%s};\n}\n@end\n' % dictString
    else:
       impString += '\n@end\n'

    del arrNameList[:]
    return impString