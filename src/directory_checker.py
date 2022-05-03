# this file will check if all the required directory exists in system. If they dosent it will create them.

import os
from pickle import FALSE, TRUE

pwd = os.getcwd()

print(pwd)

def folder_checker():

    ifdir = os.path.isdir(f"{pwd}/temp/")

    if ifdir == False:
        os.system("mkdir temp")
        print("temp folder created")


    ifdir = os.path.isdir(f"{pwd}/videos/")

    if ifdir == False:
        os.system("mkdir videos")
        print("videos folder created")

    ifdir = os.path.isdir(f"{pwd}/logs/")

    if ifdir == False:
        os.system("mkdir logs")
        print("logs folder created")