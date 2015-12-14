"""
@file appfw-python-event-send.py
"""

##
# @addtogroup app_FW app_FW
# @brief This is app_FW component
# @{
# @addtogroup appfw-python-event-send appfw-python-event-send
# @brief This is appfw-python-event-send module
# @{
##

import argparse
import json
import logging
import appfw

logger = logging.getLogger("__event-send__")

def send_status(id, status, msg, callback_data):
	"""
	@fn send_status
	@param id
	@param  msg
	@param  callback_data
	@return
	"""
	if status == 0:
		logger.debug("Event request #" + str(id) + " succesfully delivered.")
	else:
		if msg == None:
			msg = "<unknown error>"
		logger.debug("Event request #" + str(id) + "failed (" + \
		             str(id) + ": " + msg)

def simple_event_sender(app, args):
	"""
	@fn simple_event_sender
	@param app
	@param  args
	@return
	"""
	event_data = args.data
        if ',' in args.events:
            events = args.events.split(',')
        else:
            events = [args.events]
        for event in events:
             print "Sending event %s ..." % event
	     app.send_event(event, event_data, send_status, None, label=args.label,
	           appid=args.appid, binary=args.binary, 
	           user=args.user, process=args.process)

def main():
	"""
	@fn main
	@return
	"""
	#Parse arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--label", type=str, help="target application label")
	parser.add_argument("-a", "--appid", type=str, help="target application id")
	parser.add_argument("-b", "--binary", type=str, help="target application binary path")
	parser.add_argument("-u", "--user", type=str, help="target application user")
	parser.add_argument("-p", "--process", type=int, help="target application process id")
	parser.add_argument("-e", "--events", type=str, help="events to send/subscribe for")
	parser.add_argument("-q", "--quit", type=str,  default=None, help="last event to send")
	parser.add_argument("-D", "--data", type=json.loads, help="data to attach to events")
	parser.add_argument("-n", "--nevent", type=int, default=0, help="number of events to send")
	parser.add_argument("-I", "--interval", type=int, default=0, help=" between sending")
	parser.add_argument("-v", "--verbose", action="count", default=0, help="increase logging verbosity (ignored)")
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

	# Send event
        simple_event_sender(app,args)	

if __name__ == "__main__":
	main()

##
# @}
# @}
##

