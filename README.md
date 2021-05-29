# MEMS_DEMO

ffmpeg -framerate 24 -i img/test%05d.png -codec copy -b:v 1000k output1.mp4
ffmpeg -framerate 24 -i img2/test%05d.png -codec copy -b:v 1000k output2.mp4