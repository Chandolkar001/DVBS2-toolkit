import netifaces

# Get a list of all network interfaces
interfaces = netifaces.interfaces()
print(interfaces)

# Get information about a specific interface (e.g., eth0)
eth0_info = netifaces.ifaddresses('eth0')
print(eth0_info)
