from scapy.all import sniff, Ether
import os

def packet_callback(packet, named_pipe):
    payload = packet[Ether].payload
    packet_summary = f"{payload.summary()}"

    print(f"{packet_summary}")

    named_pipe.write(packet_summary + "\n")
    named_pipe.flush() 

dev = "eno1"
named_pipe_path = "frame_stream"

if not os.path.exists(named_pipe_path):
    os.mkfifo(named_pipe_path)

with open(named_pipe_path, "w") as named_pipe:
    sniff(prn=lambda pkt: packet_callback(pkt, named_pipe), iface=dev)

os.remove(named_pipe_path)