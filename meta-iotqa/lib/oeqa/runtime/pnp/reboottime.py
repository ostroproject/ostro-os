#[PROTEXCAT]
#\License: ALL RIGHTS RESERVED

"""
@file reboottime.py
"""

##
# @addtogroup pnp pnp
# @brief This is pnp component
# @{
# @addtogroup reboottime reboottime
# @brief This is reboottime module
# @{
##

import os
import time
from datetime import datetime
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.helper import collect_pnp_log

class RebootTimeTest(oeRuntimeTest):
    """The case will measure system reboot time
    @class RebootTimeTest
    """

    
    def test_reboottime(self):
        """Measure system reboot time
        @fn test_reboottime
        @param self
        @return
        """
        filename = os.path.basename(__file__)
        casename = os.path.splitext(filename)[0]
        (status, out)=self.target.run('date +"%m-%d %H:%M:%S"; reboot &')
        print "\nReboot start time: %s\n" % (out)
        start_t = datetime.strptime(out,"%m-%d %H:%M:%S")
        #print start_t
        time.sleep(60)
        
        (status, out)=self.target.run("journalctl -b -a >/tmp/system.log")
        ##
        # TESTPOINT: #1, test_reboottime
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % out)
        (status, out)=self.target.run(" cat /tmp/system.log | "
                "grep 'Starting Login' | "
                "awk '{print $1, $2, $3}'")
        ##
        # TESTPOINT: #2, test_reboottime
        #
        self.assertEqual(status, 0, msg="Error messages: %s" % out)
 
        print "\nReboot end time: %s\n" % (out)
        end_t = datetime.strptime(out,"%b %d %H:%M:%S")
        #print end_t
        used_t = end_t -start_t
        reboot_time = used_t.total_seconds()
        reboot_time_str = str(reboot_time) + "s"
       
        if(reboot_time <= 0):
            print "please check system date:\n"
            print reboot_time_str
            ##
            # TESTPOINT: #3, test_reboottime
            #
            self.assertEqual(-1, 0, reboot_time_str)
        else:
            collect_pnp_log(casename, casename, reboot_time_str)
            print "\n%s:%s\n" % (casename, reboot_time_str)
            ##
            # TESTPOINT: #4, test_reboottime
            #
            self.assertEqual(status, 0, reboot_time_str)



##
# @}
# @}
##

