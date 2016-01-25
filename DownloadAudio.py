#! /usr/bin/python
#Author: Hardhik Mallipeddi
#Made to ease the download process. No copyright infringement intended.
import re
import os

__DIR__ = './songs/' # Enter the directory in which you want to download the songs
if not os.path.exists(__DIR__):
    os.makedirs(__DIR__)

p= re.compile('https:*')
FilePointer = open("README.md")
lines=[]
for i in FilePointer.readlines():
    lines.append(i[:-1]) # -1 to remove the '\n' that comes along

for i in lines:
    m = p.search(i)
    if(m is not None):
        url = i[m.start():-1] # -1 to remove the ')' present in end of line 
        args = '-o "songs/%(title)s.%(ext)s" --extract-audio --audio-format mp3 --prefer-ffmpeg -w ' + url
        os.system("youtube-dl "+args)
