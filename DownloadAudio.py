#! /usr/bin/python

import re
import os

p= re.compile('https:*')
FilePointer = open("README.md")
lines=[]
for i in FilePointer.readlines():
    lines.append(i[:-1]) # -1 to remove the '\n' that comes along

for i in lines:
    m = p.search(i)
    if(m is not None):
        url = i[m.start():-1] # -1 to remove the ')' present in end of line 
        #print url
        args = "--extract-audio --audio-format mp3 --prefer-ffmpeg -w "+url
        os.system("youtube-dl "+args)
