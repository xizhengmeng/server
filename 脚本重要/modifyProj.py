from mod_pbxproj import XcodeProject

project = XcodeProject.Load('/Users/wxg/Documents/JDMobile/JDMobile_2.0/JDMobile.xcodeproj/project.pbxproj')

for item in project.objects.values():
    nameIsa = item.get('isa')
    
    if (nameIsa == 'XCBuildConfiguration'):
        setting = item.get('buildSettings')
        nameReference = item.get('baseConfigurationReference')
        if (nameReference):
           idStr = setting.get('PRODUCT_BUNDLE_IDENTIFIER')
           print '---->' + idStr
           setting.__setitem__('PRODUCT_BUNDLE_IDENTIFIER','com.jd.jinrong2016')
           setting.__setitem__('PROVISIONING_PROFILE','')
           setting.__setitem__('PROVISIONING_PROFILE_SPECIFIER','')
           setting.__setitem__('DEVELOPMENT_TEAM','5TKVHWTT79')
           item.__setitem__('buildSettings',setting)
        else:
           codeSign = setting.get('CODE_SIGN_IDENTITY')
           profile = setting.get('PROVISIONING_PROFILE')
           print codeSign
           print profile
           setting.__setitem__('CODE_SIGN_IDENTITY','iPhone Distribution: Beijing Jingdong Century Trading Co., Ltd. (TQZTTUQ9ZE)')
           setting.__setitem__('PROVISIONING_PROFILE','0d8cd55a-c922-4f27-b1aa-df6a2f277ea5')
           item.__setitem__('buildSettings',setting)

    elif (nameIsa == 'PBXProject'):
        attributes = item.get('attributes')
        targetAttributes = attributes.get('TargetAttributes')
        targets = item.get('targets')
        tar = targets[0]
        attr = targetAttributes.get('%s' % tar)
        developmentTeamName = attr.get('DevelopmentTeamName')
        developmentTeamName = attr.get('ProvisioningStyle')
        print developmentTeamName
        attr.__setitem__('DevelopmentTeamName','Beijing Jingdong Century Information Technology Co., Ltd.')
        attr.__setitem__('ProvisioningStyle', 'Automatic')
        attr.__setitem__('DevelopmentTeam', '5TKVHWTT79')

project.save()


