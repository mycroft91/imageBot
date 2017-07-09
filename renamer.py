#this section of the program handles copying and renaming of the files
import os
import re

def Image_Check(f):
    #assumes that only png files are the cards
    if f.find(".png") > -1:
        return True
    else :
        return False

def Multi_Name(f):
    #searches for Uppercase letters and if count is > 1 returns true
    return len(re.findall(r'[A-Z]',string)) > 1

def Split(f):
    wordList         = []
    f                = f[0:f.find(".png")].strip() #the image_checkroutine guanrantees that this is always valid
    matcher          = re.compile("[A-Z][^A-Z]*") #matches something in caps and the followup until the next caps
    for m in matcher.finditer(f):
        print m.start(),m.group()
        wordList.append(m.group())
    return wordList

def Renamer(directory,exceptionList={},logger=None):
    pwd              = directory
    fileList         = os.listdir(pwd)
    count            = 0
    for f in fileList:
        if Image_Check(f) and Multi_Name(f):
            name     = exceptionList.get(f,"_".join(Split(f))+".png") ##Check the exception list and rename accordingly
            os.rename(os.join(pwd,f),os.join(pwd,name))
            count   += 1
            if logger:
                logger.Print("[*]Processed-"+f+" to-"+name)
    if logger:
        logger.Echo("[*]Processed-"+str(count)+" files in "+directory)
