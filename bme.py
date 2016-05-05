from twisted.internet import task
from twisted.internet import reactor
from Adafruit_BME280 import *
import picamera

timeout = 5.0
"""
def take_photo():

    sensor = BME280(mode=BME280_OSAMPLE_8)   
    
    time = '{0:0.3f}'.format(sensor.t_fine)
    photo_file_name = 'image' + time + '.jpg'

    camera = picamera.PiCamera()
    camera.capture(photo_file_name)
"""


def read_temp():

    my_file = open('log.txt', 'a')


    sensor = BME280(mode=BME280_OSAMPLE_8)

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()
    
    timestamp = 'Timestamp = {0:0.3f}'.format(sensor.t_fine)
    temp = 'Temp = {0:0.3f} deg C'.format(degrees)
    pressure = 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
    humidity = 'Humidity  = {0:0.2f} %'.format(humidity)

    line = timestamp + "," + temp + "," + pressure + "," + humidity + "\n"

    my_file.write(line)

    
    return None

l = task.LoopingCall(read_temp)
l.start(timeout)

reactor.run()
