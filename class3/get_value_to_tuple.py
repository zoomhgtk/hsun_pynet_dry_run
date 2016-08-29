import snmp_helper
ip_addr1 = "184.105.247.70"
ip_addr2 = "184.105.247.71"

port = 161

snmp_user = 'pysnmp'
auth_key = 'galileo1'
encrypt_key = 'galileo1'

a_user = (snmp_user, auth_key, encrypt_key)

device1 = (ip_addr1, port)
device2 = (ip_addr2, port)


def get_the_current_value(device, user):
         
    ccmHistoryRunningLastChanged = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    sysUptime = '1.3.6.1.2.1.1.3.0'
    output = snmp_helper.snmp_get_oid_v3(device, user, ccmHistoryRunningLastChanged)
    last_change = snmp_helper.snmp_extract(output)
    output = snmp_helper.snmp_get_oid_v3(device, user, sysUptime)
    uptime = snmp_helper.snmp_extract(output)

    print type(last_change)
    print type(uptime)
    print last_change
    print uptime
    last_change = int(last_change)
    print type(last_change)
    uptime = int(uptime)
    print type(uptime)
    dvalue = uptime - last_change
    print "%d subtract %d is %d " % (uptime, last_change, dvalue)
    value = (last_change, uptime, dvalue)
    return value 

value1 = get_the_current_value(device1, a_user)

print value1[0], "\n", value1[1], "\n", value1[2]



