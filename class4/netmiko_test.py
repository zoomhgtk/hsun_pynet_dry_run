#!/usr/bin/env python

from netmiko import ConnectHandler

pynet1 = {
        'device_type': 'cisco_ios',
	'ip': '184.105.247.70',
	'username': 'pyclass',
	'password': '88newclass',
        }

conn1 = ConnectHandler(**pynet1)
outp = conn1.send_command("show run | inc logging")
print outp

print conn1.find_prompt()

config_commands = ['logging buffered 19999']
outp = conn1.send_config_set(config_commands)
print outp

srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'port': 22,
    'password': '88newclass',
    }

conn2 = ConnectHandler(**srx)
outp = conn2.send_command("show arp")
print outp

conn2.config_mode()
print conn2.check_config_mode()

