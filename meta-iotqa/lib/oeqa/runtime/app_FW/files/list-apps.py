"""
@file list-apps.py
"""

##
# @addtogroup app_FW app_FW
# @brief This is app_FW component
# @{
# @addtogroup list-apps list-apps
# @brief This is list-apps module
# @{
##

import argparse
import glib
import appfw
import logging
import sys
logger = logging.getLogger("__event-test__")

#Create mainloop in default context
ml = glib.MainLoop(None)

def list_callback(apps, id, status, msg, callback_data):
    """
    @fn list_callback
    @param apps
    @param  id
    @param  status
    @param  msg
    @param  callback_data
    @return
    """
    print("Got " + str(len(apps)) + " apps with id: " + str(id)  + " msg: " + str(msg) +
	   " status: " + str(status) + " callback_data: " + str(callback_data))
    for app in apps:
        print(" appid: " + str(app["appid"]) + " desktop: " + str(app["desktop"]))
    ml.quit()

def running_apps(app):
    """
    @fn running_apps
    @return
    """
    print("Requesting running apps...")
    app.list_running(list_callback, "test_callback_data")
    ml.run()

def all_apps(app):
    """
    @fn all_apps
    @return
    """
    print("Requesting all apps...")
    app.list_all(list_callback, "test_callback_data")
    ml.run()

def main():
    """
    @fn main
    @return
    """
    #Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--running", action="store_true", help="print only running applications")
    parser.add_argument("-d", "--debug", action="count", default=0, help="enable given debug configuration")
    args = parser.parse_args()

    #Create appfw context
    app = appfw.IotApp()


    if args.debug > 0:
        if args.debug >= 1:
            logging.basicConfig()
            logger.setLevel(logging.DEBUG)
        if args.debug >= 2:
            app._enable_debug([""])
        if args.debug >= 3:
            app._enable_debug(["@python-app-fw-wrapper.cpp"])
        if args.debug > 3:
            app._enable_debug(["*"])

    logger.debug(args)

    if args.running:
        running_apps(app)
    else:
        all_apps(app)

if __name__ == "__main__":
    main()

##
# @}
# @}
##

