from .models import File
from scapy.all import *
import pyshark
from collections import Counter
import traceback

def process_pcap(file : File):
    try:
        
        cap = pyshark.FileCapture(file.file.path)
        packets = []
        cnt = 0
        for pkt in cap:
            cnt += 1
            try: 
                src = pkt.IP.src + ":" + pkt.UDP.srcport
            except:
                src = "-"
            try:
                dst = pkt.IP.dst + ":" + pkt.UDP.dstport
            except:
                dst = "-"
            try:
                time_elapsed = pkt.UDP.time_relative
            except:
                time_elapsed = "-"
            protocols = list(set([x.layer_name for x in pkt.layers]))

            pkt_dir = {
                "src" : src,
                "dst": dst,
                "time_elapsed" : time_elapsed,
                "protocols" : protocols,
                
            }
            packets.append(pkt_dir)
        
        protocol_counts = Counter(protocol for pkt in packets for protocol in pkt.get("protocols", []))
        result = {
            "total" : cnt,
            "protocol_counts" : protocol_counts,
            "packets" : packets[:100], #change this
            "success" : True
        }

        return result

    except Exception as e:
        # Handle any exceptions that might occur during processing
        traceback.print_exc()
        print(e)
        return {'success': False, 'message': f'Error analyzing PCAP file: {str(e)}'}

    