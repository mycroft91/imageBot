#this section of the program handles copying and renaming of the files
import os

def image_check(f):
    #assumes that only png files are the cards
    if f.find(".png") > -1:
        return True
    else :
        return False
def multi_name(f):
    
def renamer(directory):
    pwd              = directory
    fileList         = os.listdir(pwd)
    for f in fileList:
        if image_check(f) and multi_name(f):
            name     = "_".join(split(f))
            os.rename(os.join(pwd,f),os.join(pwd,name))
