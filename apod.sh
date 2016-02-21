# display NASA astronomy pic of the day
wget http://apod.nasa.gov/apod/ --quiet -O /tmp/apod.html
grep -m 1 jpg /tmp/apod.html | sed -e 's/<//' -e 's/>//' -e 's/.*=//' -e 's/"//g' -e 's/^/http:\/\/apod.nasa.gov\/apod\//' > /tmp/pic_url
URL=`/bin/cat /tmp/pic_url`
wget --quiet $URL -O /tmp/apod.jpg
fbi -T 2 -d /dev/fb1 -noverbose -a /tmp/apod.jpg
