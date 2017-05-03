import sys,re

lines=open("ConfigManager.h",'r').readlines()
flen=len(lines)-1
for i in range(20):
   if '#define' in lines[i]:
       if '//' not in lines[i]:
          lines[i] = '//' + lines[i]

open("ConfigManager.h",'w').writelines(lines)
