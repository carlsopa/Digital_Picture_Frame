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
#global oldtrscnt
#oldtrscnt = 0
def Transfer():
    oldTotal = 0
    oldtrscnt = 0
    trscnt = (len([f for f in os.listdir(trs)]))
    oldTotal = oldTotal + trscnt
    if trscnt != 0:
        print('finally!')
        oldtrscnt = trscnt
        #oldtrscnt = 0
    print('transfer count = ' + str(trscnt))
    print('old count = ' + str(oldtrscnt))
    if (trscnt > 0) and (oldtrscnt == trscnt):
        print('COMPLETE')
    oldtrscnt = trscnt
    if trscnt > 0:
        for picture in os.listdir(trs):
            shutil.move(os.path.join(trs, picture), os.path.join(src, picture))
    print("Last total: " + str(oldTotal))

def dictfill():
    b = 0
    c = 0
    num_files = len([f for f in os.listdir(src)])
    print("number of files: " + str(num_files))
    for x in range(num_files):
        picture = (os.listdir(src)[x])
        print(picture)
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

init()
font.init()
myfont = font.SysFont("monospace",15, True)
screen = display.set_mode((0,0))
done = False
clock = time.Clock()
screen.fill((1,1,1))
    
Uploader.Testerb()
Transfer()
b,c = dictfill()
#Transfer()
while not done:
    print("START OF FIRST")
    #while (b == 0) and (c == 0):
        #label=myfont.render("No pictures to display",True,(255,255,0))
        #screen.blit(label,(100,100))
        #Uploader.Testerb()
        #Transfer()
        #if (len([f for f in os.listdir(src)]) > 0):
            #break
        #b,c = dictfill()
        #print('b = ' +str(b))
        #print('c = ' +str(c))
    #b,c = dictfill()
    if b != 0:
        bb = randint(0,b-1)
        wide1 = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide1a = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide2 = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide2a = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide3 = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide3a = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide4 = image.load(src+b_dict[bb]['Name'])
        bb = randint(0,b-1)
        wide4a = image.load(src+b_dict[bb]['Name'])
        wide1_list = [wide1,wide1a]
        wide2_list = [wide2,wide2a]
        wide3_list = [wide3,wide3a]
        wide4_list = [wide4,wide4a]
    if c != 0:
        cc = randint(0,c-1)
        tall1 = image.load(src+c_dict[cc]['Name'])
        if c_dict[cc]['Orientation'] == '6':
            tall1 = transform.rotate(tall1,270)
        cc = randint(0,c-1)
        tall1a = image.load(src+c_dict[cc]['Name'])
        if c_dict[cc]['Orientation'] == '6':
            tall1a = transform.rotate(tall1a,270)
        cc = randint(0,c-1)
        tall2 = image.load(src+c_dict[cc]['Name'])
        if c_dict[cc]['Orientation'] == '6':
            tall2 = transform.rotate(tall2,270)
        cc = randint(0,c-1)
        tall2a = image.load(src+c_dict[cc]['Name'])
        if c_dict[cc]['Orientation'] == '6':
            tall2a = transform.rotate(tall2a,270)
        tall1_list = [tall1,tall1a]
        tall2_list = [tall2,tall2a]

    while not done:
        print("START OF SECOND")

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
                bb = randint(0,b-1)
                wide1_list.pop()
                alphas3 = image.load(src+b_dict[bb]['Name'])
                wide1_list.insert(0,alphas3)
                bb = randint(0,b-1)
                wide2_list.pop()
                alphas3 = image.load(src+b_dict[bb]['Name'])
                wide2_list.insert(0,alphas3)
                bb = randint(0,b-1)
                wide3_list.pop()
                alphas3 = image.load(src+b_dict[bb]['Name'])
                wide3_list.insert(0,alphas3)
                bb = randint(0,b-1)
                wide4_list.pop()
                alphas3 = image.load(src+b_dict[bb]['Name'])
                wide4_list.insert(0,alphas3)
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
            alph = 255
            new_count = len([f for f in os.listdir(src)])
        Uploader.Testerb()
        print('second uploader')
        Transfer()
        print('second transfer')
        if (old_count != new_count):
            print('second old count: ' + str(old_count))
            print('second new count: ' + str(new_count))
            dictfill()
            old_count = new_count           

        for ev in event.get():
            if ev.type == QUIT:
                done = True
