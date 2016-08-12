import telnetlib
import time
TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(4)
	return remote_conn.read_very_eager()

def login(remote_conn, username, password=''):
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	remote_conn.write(username + '\n')
	if len(password) > 1:
		output = remote_conn.read_util("ssword:", TELNET_TIMEOUT)
		remote_conn.write(password + '\n')
	else:
		return output

	
def main():
	ip_addr = '128.223.51.103'
	username = 'rviews'
	password = ''
	
	remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	login(remote_conn, username, password)
	time.sleep(2)
	output = remote_conn.read_very_eager()
	print output
	
	output = send_command(remote_conn, 'terminal len 0') 
	output = send_command(remote_conn, 'show version')
	print output

	remote_conn.close()

if __name__ == "__main__":
	main()
