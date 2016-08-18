#! /usr/bin/env python

import snmp_helper
import sched, time
from datetime import datetime

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

#s = sched.scheduler(time.time, time.sleep)


def loop_the_oids(snmp_oids):
    for desc, each_oid, is_count in snmp_oids:
        snmp_data = snmp_helper.snmp_get_oid_v3(a_router, a_user, oid=each_oid)
        output = snmp_helper.snmp_extract(snmp_data)
        print "%s %s" % (desc, output)

def print_current_time():
    print datetime.now()

for time_range in range(1,13):
    print "time %d" % (time_range*10)
    loop_the_oids(snmp_oids)
    time.sleep(10)

'''
def run_the_loop_tasks():
    print_current_time()

    time_stemp = 100
    time_stemp += 5
    print time_stemp
    loop_the_oids(snmp_oids)
    s.enter(5, 1, run_the_loop_tasks, ())
    s.run()

run_the_loop_tasks()
'''
