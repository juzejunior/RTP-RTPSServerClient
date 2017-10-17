#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, signal
from Tkinter import Tk
from Client import Client

def signal_handler(signal, frame):
    print '\nAté Mais!'
    sys.exit(0)

if __name__ == "__main__":
	# setup terminator
	signal.signal(signal.SIGINT,signal_handler)
	try:
		serverAddr = sys.argv[1]
		serverPort = sys.argv[2]
		rtpPort = sys.argv[3]
		fileName = sys.argv[4]	
	except:
		print "[Uso: python ClientLauncher.py Server_name Server_port RTP_port Video_file]\n"
	
	root = Tk()
	
	# Create a new client
	app = Client(root, serverAddr, serverPort, rtpPort, fileName)
	app.master.title("Cliente")	
	root.mainloop()
	
