# display National Gegraphic pic of the day
wget http://photography.nationalgeographic.com/photography/photo-of-the-day/ --quiet -O- 2> /dev/null | grep -m 1 //yourshot.nationalgeographic.com/u/[^/]* -o > /tmp/pic_url
URL=`/bin/cat /tmp/pic_url`
echo $URL
wget --quiet http:$URL -O /tmp/natgeo.jpg
fbi -T 2 -d /dev/fb1 -noverbose -a /tmp/natgeo.jpg
