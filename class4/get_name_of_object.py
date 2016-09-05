from dill.source import getname

per_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'port': 22,
}

def get_name_of_obj(obj):
	for objname,oid in globals().items():
		if oid is obj:
			return objname

print get_name_of_obj(per_srx)
