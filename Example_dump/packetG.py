from scapy.all import IP, UDP, Raw, sendp, Ether

def create_ts_packet(payload):
    # Dummy ts packet with 4 byte header
    ts_packet = b'\x47' + b'\x40' + b'\x00' + b'\x00' + bytes(payload)

    return Ether(dst="01:00:00:00:00:01") / ts_packet  # Use a multicast MAC address for broadcast

http_packet = IP(dst="192.168.1.1") / UDP(dport=80) / Raw(load="GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")

http_packet_bytes = bytes(http_packet)

ts_packet = create_ts_packet(http_packet_bytes)

print("TS Packet:")
ts_packet.show()
