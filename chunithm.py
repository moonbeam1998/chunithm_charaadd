import wand.image as im
from PIL import Image
import os
import sys

def repfilecont(filepath,savepath,number,name):
    fo = open(savepath, 'w')
    fi = open(filepath, 'r', encoding='UTF-8')
    content = fi.readlines()
    for line in content:
        line = line.replace('10400', number)
        line = line.replace('Waifu', name)
        fo.write(line)
    fo.close()

def make_square(path):
    fill_color=(0, 0, 0, 1)
    img = Image.open(path)
    if img.height == img.width :
        return
    else:
        size = max(img.width, img.height)
        new_im = Image.new('RGBA', (size, size), fill_color)
        new_im.paste(img, (int((size - img.width) / 2), int((size - img.height) / 2)))
        new_im.save(path, quality = 95)
    

def png_to_dds(path, tmp, x, number):
    with im.Image(filename=path) as img:
        img.resize(tmp,tmp)
        img.format = 'dds'
        img.save(filename = ddspath + 'CHU_UI_Character_' + number + '_00_0'+ str(x) +'.dds')

number = input("number:")
name = input("name:")
epath = sys.path[0]
pathc = epath + '\\A996\\chara\\'
pathd = epath + '\\A996\\\\ddsImage\\'
os.mkdir(pathc + 'chara' + number + '0\\')
os.mkdir(pathd + 'ddsImage' + number + '0\\')
charapath = pathc + 'chara' + number + '0\\'
ddspath = pathd + 'ddsImage' + number + '0\\'
cfilepath = epath + '\\template\\Chara.xml'
dfilepath = epath + '\\template\\DDSImage.xml'
repfilecont(cfilepath, charapath + 'Chara.xml', number, name)
repfilecont(dfilepath, ddspath + 'DDSImage.xml', number, name)

dir = epath + '\\'
for imgs in os.listdir(dir):
    path = dir + "\\" + imgs
    if 'aa' in imgs:
        make_square(path)
        png_to_dds(path, 1080, 0, number)
    elif 'bb' in imgs:
        png_to_dds(path, 512, 1, number)
    elif 'cc' in imgs:
        png_to_dds(path, 128, 2, number)