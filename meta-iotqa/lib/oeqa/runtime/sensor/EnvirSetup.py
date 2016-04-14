"""
@file EnvirSetup.py
"""
##
# @addtogroup soletta sensor
# @brief This is a class used to build DUT environment
# @brief This is a class used to generate test app (.fbp file)
##

import os
import time
from oeqa.utils.helper import get_files_dir
from oeqa.oetest import oeRuntimeTest

class EnvirSetup(oeRuntimeTest):
    """
    @class EnvirSetup
    """
    def __init__(self, target):
        '''inherit target object which allow command execution on DUT
        @__init__
        @param self
        @param target
        @return'''
        self.target = target
    def envirPre(self, sensorName):
        '''push correct json to DUT and modprobe related device
        @envirPre
        @param self
        @return'''
        mkdir_path = "rm -rf /opt/apps"
        (status, output) = self.target.run(mkdir_path)
        mkdir_path = "mkdir -p /opt/apps"
        (status, output) = self.target.run(mkdir_path)
        #get board name from target
        (status, output) = self.target.run("cat /sys/devices/virtual/dmi/id/board_name")
        #modprobe target sensor on DUT
        #send corresponding correct json to DUT      
        if "Minnow" in output:
           print "DUT is MinnowMax\n"
           time.sleep(1)
           (status, output) = self.target.run("modprobe i2c-dev")
           self.assertTrue(status == 0)
           (status, output) = self.target.run("modprobe iio-trig-sysfs")
           self.assertTrue(status == 0)
           if sensorName == "mpu6050":
              (status, output) = self.target.run("modprobe i2c-minnow-mpu6050")
              self.assertTrue(status == 0)
           copy_to_path = os.path.join(os.path.dirname(__file__) + \
                          '/config/sol-flow-intel-minnow-max-linux_gt_3_17.json')
           (status, output) = self.target.copy_to(copy_to_path, \
                          "/opt/apps/")
           
        if "Galileo" in output:
           print "DUT is Galileo\n"
           time.sleep(1)
           (status, output) = self.target.run("echo -n \"60\" >/sys/class/gpio/export")
           (status, output) = self.target.run("echo -n \"out\" >/sys/class/gpio/gpio60/direction")
           (status, output) = self.target.run("echo -n \"0\" >/sys/class/gpio/gpio60/value")
           (status, output) = self.target.run("modprobe i2c-dev")
           self.assertTrue(status == 0)
           (status, output) = self.target.run("modprobe iio-trig-sysfs")
           self.assertTrue(status == 0)
           if sensorName == "mpu6050":
              (status, output) = self.target.run("modprobe i2c-quark-mpu6050")
              self.assertTrue(status == 0)
           #if sensorName == "lsm330dlc":
              #(status, output) = self.target.run("modprobe i2c-quark-lsm330dlc_gyro")
              #self.assertTrue(status == 0)
           #if sensorName == "tsl2561":
              #(status, output) = self.target.run("echo tsl2561 0x39 > /sys/bus/i2c/devices/i2c-0/new_device")
           copy_to_path = os.path.join(os.path.dirname(__file__) + '/config/sol-flow-intel-galileo-rev-g.json')
           (status, output) = self.target.copy_to(copy_to_path, \
                          "/opt/apps/")  
        if "BODEGA" in output:
           print "DUT is Edison\n"
           (status, output) = self.target.run("echo 28 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 27 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 204 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 205 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 236 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 237 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 14 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 165 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 212 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 213 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo 214 > /sys/class/gpio/export")
           (status, output) = self.target.run("echo low > /sys/class/gpio/gpio214/direction")
           (status, output) = self.target.run("echo low > /sys/class/gpio/gpio204/direction")
           (status, output) = self.target.run("echo low > /sys/class/gpio/gpio205/direction")
           (status, output) = self.target.run("echo in > /sys/class/gpio/gpio14/direction")
           (status, output) = self.target.run("echo in > /sys/class/gpio/gpio165/direction")
           (status, output) = self.target.run("echo low > /sys/class/gpio/gpio236/direction")
           (status, output) = self.target.run("echo low > /sys/class/gpio/gpio237/direction")
           (status, output) = self.target.run("echo in > /sys/class/gpio/gpio212/direction")
           (status, output) = self.target.run("echo in > /sys/class/gpio/gpio213/direction")
           (status, output) = self.target.run("echo mode1 > /sys/kernel/debug/gpio_debug/gpio28/current_pinmux")
           (status, output) = self.target.run("echo mode1 > /sys/kernel/debug/gpio_debug/gpio27/current_pinmux")
           (status, output) = self.target.run("echo high > /sys/class/gpio/gpio214/direction")
           (status, output) = self.target.run("modprobe i2c-dev")
           self.assertTrue(status == 0)
           (status, output) = self.target.run("modprobe iio-trig-sysfs")
           self.assertTrue(status == 0)
           copy_to_path = os.path.join(os.path.dirname(__file__) + '/config/sol-flow-intel-edison-rev-c.json')
           (status, output) = self.target.copy_to(copy_to_path, \
                          "/opt/apps/")

    def FBPGenerate(self, sensorType, sensorName):
        '''Generate content for FBP files
        @FBPGenerate
        @param self
        @param sensorType
        @param sensorName
        @return'''
        str_list = ['echo "#\!/usr/bin/env sol-fbp-runner" >>/opt/apps/test_', sensorType, '_', sensorName, '.fbp']
        fbpFirstLine = ''.join(str_list)
        str_list = ['sed -i \'s/\\\\//\' /opt/apps/test_', sensorType, '_', sensorName, '.fbp']
        fbpFirstLineAdjust = ''.join(str_list)
        str_list = [sensorType, '(My', sensorType.capitalize(), sensorName.capitalize(), ')']
        fbpMethodContent = ''.join(str_list)
        fbpTimer1Content = "timer1(timer:interval=1000)"
        fbpTimer2Content = "timer2(timer:interval=3000)"
        str_list = ['timer1 OUT -> TICK ', sensorType, ' OUT -> IN _(console)']
        fbpKick1Content = ''.join(str_list)
        fbpKick2Content = "timer2 OUT -> QUIT _(app/quit)"
        str_list = ['echo "', fbpMethodContent, '" >>', '/opt/apps/test_' , sensorType, '_', sensorName, '.fbp']
        fbpMethod = ''.join(str_list)
        str_list = ['echo "', fbpTimer1Content, '" >>', '/opt/apps/test_' , sensorType, '_', sensorName, '.fbp']
        fbpTimer1 = ''.join(str_list)
        str_list = ['echo "', fbpTimer2Content, '" >>', '/opt/apps/test_' , sensorType, '_', sensorName, '.fbp']
        fbpTimer2 = ''.join(str_list)
        str_list = ['echo "', fbpKick1Content, '" >>', '/opt/apps/test_' , sensorType, '_', sensorName, '.fbp']
        fbpKick1 = ''.join(str_list)
        str_list = ['echo "', fbpKick2Content, '" >>', '/opt/apps/test_' , sensorType, '_', sensorName, '.fbp']
        fbpKick2 = ''.join(str_list)
        str_list = [fbpFirstLine, '; ', fbpFirstLineAdjust, '; ', fbpMethod, '; ', \
                    fbpTimer1, '; ',fbpTimer2, '; ', fbpKick1, '; ', fbpKick2]
        self.fbpFile = ''.join(str_list)
        #print "fbpFile: \n" + self.fbpFile + "\n"
    def envirSetup(self, sensorName, sensorType):
        '''Generate .fbp file on target DUT
        @envirSetup
        @param self
        @param sensorName
        @param sensorType
        @return'''
        #make sure sensor is detected and push correct json to DUT
        self.envirPre(sensorName)
        #generate corresponding fbp file
        self.FBPGenerate(sensorType, sensorName)
        self.target.run(self.fbpFile)
