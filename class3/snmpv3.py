#! /usr/bin/env python

import snmp_helper

'''
pynet-rtr2#sho snmp user

User name: pysnmp
Engine ID: 8000000903001C6A7AAF5768
storage-type: nonvolatile active
Authentication Protocol: SHA
Privacy Protocol: AES128
Group-name: READONLY
'''


OID = '1.3.6.1.2.1.1.5.0'

ip_addr = '184.105.247.70'
port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'


a_user = (snmp_user, auth_key, encrypt_key)
a_device = (ip_addr, port)

snmp_data = snmp_helper.snmp_get_oid_v3(a_device, a_user, OID)
output = snmp_helper.snmp_extract(snmp_data)

print output
