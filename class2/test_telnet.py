#!/usr/bin/env python

import telnetlib
import time
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
	ip_addr = '128.223.51.103'
	username = 'rviews'
	password = ''
	
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	remote_conn.write(username + '\n')
	time.sleep(2)
	output = remote_conn.read_very_eager()
	print output
	
	remote_conn.write("terminal len 0" + '\n')
	time.sleep(2)
	remote_conn.write("show version"+ '\n')
	time.sleep(4)
	output = remote_conn.read_very_eager()
	print output

if __name__ == "__main__":
	main()

