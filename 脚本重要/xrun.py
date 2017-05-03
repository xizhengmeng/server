import os,shutil

os.mkdir('Payload')

shutil.copytree('JDMobile.app','Payload/JDMobile.app')

os.system('zip -r Payload.zip Payload')

files=os.listdir(".")

for filename in files:
    li=os.path.splitext(filename)
    if li[1]==".zip":
        newname=li[0]+".ipa"
        os.rename(filename,newname)

shutil.rmtree('JDMobile.app')
shutil.rmtree('Payload')

