"""
@file Connector.py
"""
##
# @addtogroup soletta sensor
# @brief use TCOB to physically connect DUT and target sensor 
##

import serial
import sys, os
import ConfigParser

class Connector:
    """
    @class Connector
    """
    def __init__(self, config_file_path):
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_path)
        s = cf.sections()
        print s
        sda_value = cf.get(sys.argv[1], 'SDA')
        scl_value = cf.get(sys.argv[1], 'SCL')
        int_value = ''
        try:
          int_value = cf.get(sys.argv[1], 'INT')
          print int_value
        except Exception,ex:
          print Exception, ":", ex
        print sda_value, scl_value
        device = serial.Serial('/dev/ttyACM1',9600)
        #reset board
        reset = device.write('switch_reset\n')
        #connect DUT to board
        SCL = device.write('now_switch_on 0 0 0\n')
        SDA = device.write('now_switch_on 0 1 1\n')
        INT = device.write('now_switch_on 0 2 2\n')
        #connect target sensor to board
        senosr_SCL = device.write('now_switch_on ' + scl_value.replace('\'','') + ' 0\n')
        sensor_SDA = device.write('now_switch_on ' + sda_value.replace('\'','') + ' 1\n')
        if int_value != '':
           print 'need conenct INT!!!\n'
           sensor_INT = device.write('now_switch_on ' + int_value.replace('\'','') + ' 2\n')
            
print 'start!'
print os.path.dirname(__file__) + '/config/sensorPin.ini'
t = Connector(os.path.dirname(__file__) + '/config/sensorPin.ini')
