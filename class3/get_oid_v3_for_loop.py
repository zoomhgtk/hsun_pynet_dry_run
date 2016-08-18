#! /usr/bin/env python
import snmp_helper

snmp_oids = (
        ('sysName', '1.3.6.1.2.1.1.5.0', None),
        ('sysUptime', '1.3.6.1.2.1.1.3.0', None),
        ('ifDescr_fa4', '1.3.6.1.2.1.2.2.1.2.5', None),
        ('ifInOctets_fa4', '1.3.6.1.2.1.2.2.1.10.5', True),
        ('ifInUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.11.5', True),
        ('ifOutOctets_fa4', '1.3.6.1.2.1.2.2.1.16.5', True),
        ('ifOutUcastPkts_fa4', '1.3.6.1.2.1.2.2.1.17.5', True),
)

ip_addr = '184.105.247.70'
port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)
a_router = (ip_addr, port) 

for desc, each_oid, is_count in snmp_oids:
    snmp_data = snmp_helper.snmp_get_oid_v3(a_router, a_user, oid=each_oid)
    output = snmp_helper.snmp_extract(snmp_data)
    print "%s %s" % (desc, output)
