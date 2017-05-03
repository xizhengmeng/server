from django.core.mail import send_mail

itemNameList = []

def getCreatedStringWithProperties(propertyString):
    propertyList = propertyString.split('\n')
    resultString = ''
    
    global itemNameList
    itemNameList = []

    for item in propertyList:
        resultString += changeItemToImpString(item)

    createSubString = '- (void)createSubViews {\n'
    for item in itemNameList:
        itemString = '[self addSubview:self.%s];\n' % item
        createSubString += itemString

    createSubString += '}\n\n'

    layoutSubViewsString = '- (void)layoutSubviews {\n'
    for item in itemNameList:
        itemString = 'self.%s.x_jr = 0;\nself.%s.y_jr = 0;\n\n' % (item,item)
        layoutSubViewsString += itemString
    layoutSubViewsString += '}\n\n'

    commonString1 = '- (instancetype)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier {\nif (self = [super initWithStyle:style reuseIdentifier:reuseIdentifier]) {\n[self createSubViews];\n}\nreturn self;\n}\n\n'

    commonString2 = '- (instancetype)initWithFrame:(CGRect)frame {\nif (self = [super initWithFrame:frame]) {\nself.backgroundColor = [UIColor jrColorWithHex:@"#FFFFFF"];\n[self createSubViews];\n}\nreturn self;\n}\n\n'

    resultString = commonString1 + commonString2 + createSubString + layoutSubViewsString + '\n#pragma mark - getter and setter' + resultString

    return resultString

def changeItemToImpString(itemString):
    global itemNameList
    itemString = itemString.encode('utf-8')
    stringList = itemString.split(')')
    if (len(stringList) == 0):
        return ''

    lastString = stringList[-1]
    typeString = lastString.split('*')[0]
    typeString = typeString.replace(' ','')

    nameString = lastString.split('*')[-1]
    nameString = nameString.replace(' ','')
    nameString = nameString.replace(';','')

    itemNameList.append(nameString)

    impstring = createImpStringWithTypeString(typeString, nameString)
    print impstring
    return impstring

def createImpStringWithTypeString(typeSring, nameString):
    if (typeSring == 'UIButton'):
        return '\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [UIButton buttonWithType:UIButtonTypeCustom];\n[_%s addTarget:self action:@selector(%sClick) forControlEvents:UIControlEventTouchUpInside];\n[_%s setTitleColor:[UIColor jrColorWithHex:@"#508CEE"] forState:UIControlStateNormal];\n_%s.titleLabel.font = [UIFont getSystemFont:10 Weight:KFontWeightRegular];\n}return _%s;\n} \n\n - (void)%sClick {\nif (self.%sBlock) {\nself.%sBlock();\n}\n}\n\n@property (nonatomic, copy) void (^%sBlock)();' % (typeSring, nameString, nameString, nameString, nameString,nameString,nameString,nameString,nameString,nameString,nameString,nameString,nameString)
    elif (typeSring == 'UIView'):
        return '\n\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [[UIView alloc] init];\n _%s.size_jr = CGSizeMake(0,0);\n _%s.backgroundColor = [UIColor jrColorWithHex:@\"#ffffff\"];\n}\nreturn _%s;\n}' % (typeSring, nameString, nameString, nameString,nameString ,nameString, nameString)
    elif (typeSring == 'UIImageView'):
        return '\n\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [[UIImageView alloc] initWithFrame:CGRectMake(0,0,0,0)];\n}\nreturn _%s;\n}' % (typeSring, nameString, nameString, nameString,nameString)
    elif (typeSring == 'NSMutableArray'):
        return '\n\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [NSMutableArray array];\n}\nreturn _%s;\n}' % (typeSring, nameString, nameString, nameString,nameString)
    elif (typeSring == 'UILabel'):
        return '\n\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [[UILabel alloc] init];\n_%s.font = [UIFont getSystemFont:10 Weight:KFontWeightRegular];\n _%s.textColor = [UIColor jrColorWithHex:@\"#ffffff\"];\n}\nreturn _%s;\n}' % (typeSring, nameString, nameString, nameString,nameString ,nameString, nameString)
    elif (typeSring == 'UITextField'):
        return '\n\n\n- (%s *)%s {\nif (!_%s) {\n_%s = [[UITextField alloc] init];\n_%s.size_jr = CGSizeMake(0, 0);\n _%s.placeholder = @"";\n_%s.layer.borderColor = [UIColor jrColorWithHex:@"#DDDDDD"].CGColor;\n_%s.layer.borderWidth = 0.5;\n_%s.font = [UIFont getSystemFont:16 Weight:KFontWeightRegular];\n_%s.textColor = [UIColor jrColorWithHex:@"#333333"];\n}\nreturn _%s;\n}' % (typeSring, nameString, nameString, nameString,nameString ,nameString, nameString,nameString,nameString,nameString,nameString)
    else:
        return ''
