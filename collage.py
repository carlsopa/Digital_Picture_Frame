#!/usr/bin/python
import pygame, sys
from pygame import *
import os.path
import PIL
import piexif
from testba import *
from PIL import Image
from random import randint
global b
global c
global b_dict
global c_dict
b_dict = {}
c_dict = {}
src = '/mnt/usb/usb/www/html/Frame/Photos/'
trs = '/mnt/usb/usb/www/html/uploads/'
b = 0
c = 0
x = 0
y = 0
alph = 255
rotate = 0
old_count = len([f for f in os.listdir(src)])
new_count = 0

def Transfer():
    trscnt = (len([f for f in os.listdir(trs)]))
    if trscnt > 0:
        for picture in os.listdir(trs):
            shutil.move(os.path.join(trs, picture), os.path.join(src, picture))

def dictfill():
    #B: photos taken in landscape
    #C: photos taken in portrait
    b = 0
    c = 0
    num_files = len([f for f in os.listdir(src)])
    print("number of files: " + str(num_files))
    for x in range(num_files):
        picture = (os.listdir(src)[x])
        #print("x name: "+x)
        #print("picture name: "+picture)
        im = Image.open(src+picture)
        exif_dict = piexif.load(im.info['exif'])
        if 274 in exif_dict['0th']:
            if exif_dict['0th'][274] == 6:
                c_dict[c] = {'Orientation' : '6', 'Name': picture, 'Width': im.size[0], 'Height': im.size[1]}
                c +=1
            if exif_dict['0th'][274] == 1:
                b_dict[b] = {'Orientation' : '1', 'Name': picture, 'Width': im.size[0], 'Height': im.size[1]}
                b += 1
        else:
            c_dict[c] = {'Orientation' : '0', 'Name': picture, 'Width': im.size[0], 'Height': im.size[1]}
            c += 1
    print('b total: ' + str(b))
    print('c total: ' + str(c))
    return b,c

def DictionaryCount(X):
    bb = randint(0,b-1)
    while bb in X:
        bb = randint(0,b-1)
    X.append(bb)
    return X, image.load(src+b_dict[bb]['Name']), bb

def DictionaryCountA(A,B):
    A.pop()
    B, C, D = DictionaryCount(B)
    A.insert(0,C)
    return A,B,C

def TallDictionaryCount(X):
    cc = randint(0,c-1)
    while cc in X:
        cc = randint(0,c-1)
    X.append(cc)
    tall1 =  image.load(src+c_dict[cc]['Name'])
    if c_dict[cc]['Orientation'] == '6':
        tall1 = transform.rotate(tall1,270)
    return X, tall1
        
init()
#screen = display.set_mode((0,0),pygame.FULLSCREEN)
screen = display.set_mode((0,0))
done = False
clock = time.Clock()
    
Uploader.Testerb()
Transfer()
b,c = dictfill()
while not done:
    if b != 0:
        RandomBList = []
        RandomBList,wide1,bb = DictionaryCount(RandomBList)
        RandomBList,wide1a,bb = DictionaryCount(RandomBList)      
        RandomBList,wide2,bb = DictionaryCount(RandomBList)      
        RandomBList,wide2a,bb = DictionaryCount(RandomBList)
        RandomBList,wide3,bb = DictionaryCount(RandomBList)
        RandomBList,wide3a,bb = DictionaryCount(RandomBList)
        RandomBList,wide4,bb = DictionaryCount(RandomBList)
        RandomBList,wide4a,bb = DictionaryCount(RandomBList)
        print("Random List B: ",RandomBList)
        wide1_list = [wide1,wide1a]
        wide2_list = [wide2,wide2a]
        wide3_list = [wide3,wide3a]
        wide4_list = [wide4,wide4a]
    if c != 0:
        RandomCList=[]
        cc = randint(0,c-1)
        RandomCList, tall1 = TallDictionaryCount(RandomCList)
        RandomCList, tall1a = TallDictionaryCount(RandomCList)
        RandomCList, tall2 = TallDictionaryCount(RandomCList)
        RandomCList, tall2a = TallDictionaryCount(RandomCList)
        tall1_list = [tall1,tall1a]
        tall2_list = [tall2,tall2a]

    while not done:
        if alph > 0:
            alph -= 10
            if b != 0:
                wide1_list[1].set_alpha(alph)
                wide1_list[1]= transform.scale(wide1_list[1],(515,328))
                wide1_list[0]= transform.scale(wide1_list[0],(515,328))
                wide2_list[1].set_alpha(alph)
                wide2_list[1]= transform.scale(wide2_list[1],(515,328))
                wide2_list[0]= transform.scale(wide2_list[0],(515,328))
                wide3_list[1].set_alpha(alph)
                wide3_list[1]= transform.scale(wide3_list[1],(515,328))
                wide3_list[0]= transform.scale(wide3_list[0],(515,328))
                wide4_list[1].set_alpha(alph)
                wide4_list[1]= transform.scale(wide4_list[1],(515,328))
                wide4_list[0]= transform.scale(wide4_list[0],(515,328))
            if c != 0:
                tall1_list[1].set_alpha(alph)
                tall1_list[1]= transform.scale(tall1_list[1],(328,515))
                tall1_list[0]= transform.scale(tall1_list[0],(328,515))
                tall2_list[1].set_alpha(alph)
                tall2_list[1]= transform.scale(tall2_list[1],(328,515))
                tall2_list[0]= transform.scale(tall2_list[0],(328,515))
            if b != 0:
                screen.blit(wide1_list[0],(137, 0))
                screen.blit(wide1_list[1],(137, 0))
                screen.blit(wide2_list[0],(559, 609))
                screen.blit(wide2_list[1],(559, 609))
                screen.blit(wide3_list[0],(1168, 95))
                screen.blit(wide3_list[1],(1168, 95))
                screen.blit(wide4_list[0],(1168, 517))
                screen.blit(wide4_list[1],(1168, 517))
            if c != 0:
                screen.blit(tall1_list[0],(137, 421))
                screen.blit(tall1_list[1],(137, 421))
                screen.blit(tall2_list[0],(746, 0))
                screen.blit(tall2_list[1],(746, 0))

            display.flip()
        else:
            if b != 0:
                print('b fill')
                RandomBList = []
                wide1_list,RandomBList,alphas3 = DictionaryCountA(wide1_list,RandomBList)
                wide2_list,RandomBList,alphas3 = DictionaryCountA(wide2_list,RandomBList)
                wide3_list,RandomBList,alphas3 = DictionaryCountA(wide3_list,RandomBList)
                wide4_list,RandomBList,alphas3 = DictionaryCountA(wide4_list,RandomBList)
                print("Random List B: ",RandomBList)
                print('before crash')
            if c != 0:
                print('c fill')
                cc = randint(0,c-1)
                tall1_list.pop()
                alphas3 = image.load(src+c_dict[cc]['Name'])
                if c_dict[cc]['Orientation'] == '6':
                    alphas3 = transform.rotate(alphas3,270)
                tall1_list.insert(0,alphas3)
                cc = randint(0,c-1)
                tall2_list.pop()
                alphas3 = image.load(src+c_dict[cc]['Name'])
                if c_dict[cc]['Orientation'] == '6':
                    alphas3 = transform.rotate(alphas3,270)
                tall2_list.insert(0,alphas3)
            Transfer()
            Uploader.Testerb()
            new_count = len([f for f in os.listdir(src)])
            if (old_count != new_count):
                dictfill()
                old_count = new_count
            alph = 255

            #new_count = len([f for f in os.listdir(src)])
            #Uploader.Testerb()
    print('i hate you')
    Transfer()
    if (old_count != new_count):
        dictfill()
        old_count = new_count           

    for ev in event.get():
        if ev.type == QUIT:
            done = True
