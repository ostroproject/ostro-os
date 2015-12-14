#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file poweroff.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup poweroff poweroff
# @brief This is poweroff module
# @{
##

import os
import serial
import time
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class PoweroffTest(oeRuntimeTest):
    """The case will measure power off time,
    which requires hardware devices (Arduino and relay).
    Please set up required devices before collecting data!
    @class PoweroffTest
    """

    
    def test_poweroff(self):
        """Measure system power off time
        @fn test_poweroff
        @param self
        @return
        """
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        port = "/dev/ttyACM0"
        running = True
        search_s = "Poweroff time: "
    
        ser = serial.Serial(port, 9600, timeout=5.0)
        time.sleep(2)       #wait for serial port available
        ser.write('s')      #ask arduino to check power singnal
        (status, out)=self.target.run('poweroff &')
        while running:
            data = ser.readline()
            print data
            i = data.find(search_s)
            if (i != -1):
                running = False
                time_p = data[(i+len(search_s)):]

        poweroff_t = str(float(time_p)/1000.0) + "s"
        collect_pnp_log(casename, casename, poweroff_t)
        print "\n%s:%s\n" % (casename, poweroff_t)
        ##
        # TESTPOINT: #1, test_poweroff
        #
        self.assertEqual(status, 0, poweroff_t)

        ser.write('o')      #ask arduino to power on device
        ser.close()

##
# @}
# @}
##

