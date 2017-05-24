import os
import shutil
from pathlib import Path
import glob
from time import sleep
from subprocess import call

from tkinter import *
root = Tk()
v = StringVar()
Label(root, textvariable=v).pack()
#empty list to hold the titles of the pictures from the incomding media
title = []
#setup location variables to receive and send pictures
dst = '/mnt/usb/usb/Photos'
class Uploader(object):
    def Testerb():
        directory = glob.glob('/media/pi/*')
        print(directory)
        if len(directory) > 1:
            #v.set("Media device found, checking for photos")
            src = directory[0]
            print(src)
            cnt = len(os.listdir(src))
            #runs a loop for on the incoming media, pulling and storing the titles of all
            #the images.
            for x in range(cnt):
                pic_title = (os.listdir(src)[x])
                title.append(pic_title)
                print(x)
            #runs a loop over the incoming media, checking to see if the file exists in the
            #main folder.  If it does not exist it will create a copy there.
            for x in range(cnt):
                if not Path(dst+title[x]).is_file():
                    shutil.copy(src+'/'+title[x],dst)
            #call(["umount",src])
            v.set("Transfer complete, please remove media device")
            root.after(10000,root.destroy)
            root.mainloop()
        #sleep(15)
