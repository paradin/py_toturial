#! /usr/bin/env python
# -*- utf-8 -*-

import socket
import sys

def whoseip(argv):
	if len(argv) < 2:
		print "Useage: whoseip ip1 ip2..."
	else:
		for i,ip in enumerate(argv):
			if i>0:
				try:
					print "" + argv[i] + "->" + socket.gethostbyaddr(argv[i])[0]
				except:
					print "Fail to find: " + argv[i]

if __name__=="__main__":
	whoseip(sys.argv)

