import subprocess
import json
import argparse
import os

###Set some input arguments. https://docs.python.org/3/howto/argparse.html

parser = argparse.ArgumentParser()

parser.add_argument("inputvideo")

args = parser.parse_args()

usrinputvideo = args.inputvideo
usrinputvideoname = os.path.splitext(usrinputvideo)[0]
usrinputframespath = usrinputvideoname


###Probe the video and parse the output as JSON

#.\ffmpeg\ffprobe.exe -i <<INPUTVIDEOPATH>> -print_format json -loglevel fatal -show_streams -count_frames -select_streams v
ffprober = ".\\ffmpeg\\ffprobe.exe -i " + usrinputvideo + " -print_format json -loglevel fatal -show_streams -count_frames -select_streams v"

result = subprocess.check_output(ffprober, shell=True)
ffproberparsed = json.loads(result)

#Grab the average frame rate. avg_frame_rate is used instead of r_frame_rate 
#to try to account for VFR content
framerate = ffproberparsed['streams'][0]['avg_frame_rate']
print(framerate)


###Make a temp video with no audio

#.\ffmpeg\ffmpeg.exe -r <<INPUTVIDEOFPS>> -f image2 -pix_fmt yuv420p -i .\frames\<<INPUTVIDEONAME>>\<<INPUTVIDEONAME>>-%07d.png -vcodec libx264 -crf 17 -pix_fmt yuv420p -y <<INPUTVIDEONAME>>-temp.mp4
ffmuted = ".\\ffmpeg\\ffmpeg.exe -r " + framerate + " -f image2 -pix_fmt yuv420p -i .\\frames\\" + usrinputframespath + "\\" + usrinputframespath + "-%07d.png -vcodec libx264 -crf 17 -pix_fmt yuv420p -y " + usrinputvideoname + "-temp.mp4"
result = subprocess.check_output(ffmuted, shell=True)


###Glue together the audio and the temp video

#.\ffmpeg\ffmpeg.exe -I <<INPUTVIDEONAME>>-temp.mp4 -i <<INPUTVIDEOPATH>> -map 0:v:0? -map 1? -map -1:v? -c copy -pix_fmt yuv420p <<INPUTVIDEONAME>>-glued.mp4 -y
ffglue = ".\\ffmpeg\\ffmpeg.exe -i " + usrinputvideoname + "-temp.mp4 -i " + usrinputvideo + " -map 0:v:0? -map 1? -map -1:v? -c copy -pix_fmt yuv420p " + usrinputvideoname + "-glued.mp4 -y"
result = subprocess.check_output(ffglue, shell=True)


###Remove the temp video with no audio

try:
	os.remove(usrinputvideoname + "-temp.mp4")
except OSError:
	pass
