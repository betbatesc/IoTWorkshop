from bluetooth import *

"""
	A Bluetooth device is uniquely identified by its address.
	Bluetooth Address is represented as a string in the form: "XX:XX:XX:XX:XX:XX"
"""

# user-friendly device name
target_name = "LG G5 SE"
target_address = None

# scan nearby devices
nearby_devices = discover_devices(duration = 8, flush_cache = True)

# connect to each device and request its user-friendly device name
for address in nearby_devices:	
	if target_name == lookup_name(address, timeout = 10):
		target_address = address
		break
		
if target_address is not None:
	print("Found target bluetooth device with address", target_address)
else:
	print("Could not find target bluetooth device nearby")
