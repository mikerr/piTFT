# grab current frame, display and exit
python mjpeg.py cctv:8081 webcam.jpg
fbi -T 2 -d /dev/fb1 -noverbose -a webcam.jpg
