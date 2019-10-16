# VideoDumpty CLI
Break apart a video into frames, modify them, then recombine the frames back into video with the original framerate and audio.

## Requirements
* Windows only (for now)
* ffmpeg
* python

## Directions
First, download [ffmpeg](https://ffmpeg.org/download.html) and put ```ffmpeg.exe``` and ```ffprobe.exe``` in the ```.\ffmpeg``` folder
* Enter ```python dumptybreak.py panda.mp4``` to "break apart" a video into its composite frames. The extracted frames will appear in ```.\frames\panda``` (using the name of the input video)
* Modify the extracted frames any way you like, but keep the filenames and number of frames the same.
* Enter ```python dumptyglue.py panda.mp4``` to generate a new video from the frames found in ```.\frames\panda``` using the framerate and audio from ```panda.mp4``` called ```panda-glued.mp4```.

## Known issues
* I suck at Python
* There is a colorspace adjustment during the conversion that needs to be ironed out
* Filenames cannot contain spaces
