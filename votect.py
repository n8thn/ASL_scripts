#!/usr/bin/python
#n8thn 2017
import os
import RPi.GPIO as GPIO
import time
import sys
if os.path.exists('/etc/asterisk/votectpy.conf'):
	execfile('/etc/asterisk/votectpy.conf')
else:
	print "System votectpy.conf does not exists"
	sys.exit()
if os.path.isdir('/tmp/voter'):
	pass
else:
	os.mkdir('/tmp/voter')
if os.path.exists('/tmp/voter/votect.ulaw'):
	os.unlink('/tmp/voter/votect.ulaw')
os.symlink (cti,'/tmp/voter/votect.ulaw')

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pin8, GPIO.IN, pull_up_down=GPIO.PUD_UP)

a = GPIO.input(pin1)
b = GPIO.input(pin2)
c = GPIO.input(pin3)
d = GPIO.input(pin4)
e = GPIO.input(pin5)
f = GPIO.input(pin6)
g = GPIO.input(pin7)
h = GPIO.input(pin8)
count = 0
time.sleep(1) #kerchunk delay time

while os.path.exists('/tmp/RPT_RXKEYED'):
	a = a + GPIO.input(pin1)
	b = b + GPIO.input(pin2)
	c = c + GPIO.input(pin3)
	d = d + GPIO.input(pin4)
	e = e + GPIO.input(pin5)
	f = f + GPIO.input(pin6)
	g = g + GPIO.input(pin7)
	h = h + GPIO.input(pin8)
	count = count + 1
if a < b and a < c and a < d and a < e and a < f and a < g and a < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
		os.unlink('/tmp/voter/votect.ulaw')
	os.symlink (cta,'/tmp/voter/votect.ulaw')
elif b < a and b < c and b < d and b < e and b < f and b < g and b < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
        	os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctb,'/tmp/voter/votect.ulaw')
elif c < a and c < b and c < d and c < e and c < f and c < g and c < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
        	os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctc,'/tmp/voter/votect.ulaw')
elif d < a and d < b and d < c and d < e and d < f and d < g and d < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
	        os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctd,'/tmp/voter/votect.ulaw')
elif e < a and e < b and e < c and e < d and e < f and e < g and e < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
	        os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (cte,'/tmp/voter/votect.ulaw')
elif f < a and f < b and f < c and f < d and f < e and f < g and f < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
	        os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctf,'/tmp/voter/votect.ulaw')
elif g < a and g < b and g < c and g < d and g < e and g < f and g < h:
	if os.path.exists('/tmp/voter/votect.ulaw'):
        	os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctg,'/tmp/voter/votect.ulaw')
elif h < a and h < b and h < c and h < d and h < e and h < f and h < g:
	if os.path.exists('/tmp/voter/votect.ulaw'):
	        os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (cth,'/tmp/voter/votect.ulaw')
else:
	if os.path.exists('/tmp/voter/votect.ulaw'):
	        os.unlink('/tmp/voter/votect.ulaw')
        os.symlink (ctj,'/tmp/voter/votect.ulaw')

if (logfile is 'yes'):
	file = open("/tmp/votectpy.txt","a+")
	file.write ( 'pin1=' + repr(a) + ' pin2=' + repr(b) + ' pin3=' + repr(c) + ' pin4=' + repr(d) + ' pin5=' + repr(e) + ' pin6=' + repr(f) + ' pin7=' + repr(g) + ' pin8=' + repr(h) + '\n' )
file.close()
