import subprocess
import json
import argparse
import os


###Set some input arguments. https://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()
parser.add_argument("inputvideo")
args = parser.parse_args()
#To do: handle spaces on filenames better
usrinputvideo = args.inputvideo
usrinputvideoname = os.path.splitext(usrinputvideo)[0]


###Make a directory to put the frames into based on the name of the input video

if not os.path.exists(".\\frames\\" + usrinputvideoname):
    os.makedirs(".\\frames\\" + usrinputvideoname)


###Gimmie the frames

#Use this line for frames scaled to a maximum width of 200px. Scaled frames 
#can be easier to use in some cases, such as with machine learning.
#.\ffmpeg\ffmpeg.exe -i <<INPUTVIDEOPATH>> -vf scale='min(200,iw)':-2 .\frames\<<INPUTVIDEONAME>>\<<INPUTVIDEONAME>>-%07d.png

#Use this line for full-size frames
framebreak=".\\ffmpeg\\ffmpeg.exe -i " + usrinputvideo + " .\\frames\\" + usrinputvideoname + "\\" + usrinputvideoname + "-%07d.png"
result = subprocess.check_output(framebreak, shell=True)
