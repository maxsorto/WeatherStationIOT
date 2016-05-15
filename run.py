import time, bme

print '\nRunning this script takes temperature, pressure'
print 'and humidity reading every 15 minutes'
print 'along with an image capture. \n'
print "The data is stored in 'log.txt' and the images in the 'imgs' /n"
print 'folder both found at the root of this script.'
print '\n'

while True:
    bme.read_temp()
    time.sleep(15)



