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
                "number" : pkt.number,
                "src" : src,
                "dst": dst,
                "time_elapsed" : time_elapsed,
                "protocols" : protocols,
                "length" : pkt.length,
                # "info" : pkt.info,
                
            }
            packets.append(pkt_dir)
        
        protocol_counts = Counter(protocol for pkt in packets for protocol in pkt.get("protocols", []))
        result = {
            "file_id" : file.id,
            "total" : cnt,
            "protocol_counts" : protocol_counts,
            "packets" : packets[:1000], #change this
            "success" : True
        }

        return result

    except Exception as e:
        # Handle any exceptions that might occur during processing
        traceback.print_exc()
        print(e)
        return {'success': False, 'message': f'Error analyzing PCAP file: {str(e)}'}

    
def get_extra_data(file, id):
    cap = pyshark.FileCapture(file.file.path)
    packet = cap[id-1]
    result = []
    layers = packet.layers

    for pkt in layers:
        if hasattr(pkt, "pid"):
            pid = pkt.pid if hasattr(pkt, 'pid') else 'N/A'
            cc = pkt.cc if hasattr(pkt, 'cc') else 'N/A'
            tsc = pkt.tsc if hasattr(pkt, 'tsc') else 'N/A'
            result.append({
                "pid": pid,
                "cc": cc,
                "tsc": tsc
            })

    return result


def new_extra_data(file, id):
    cap = pyshark.FileCapture(file.file.path)
    packet = cap[id-1]
    result = []
    layers = packet.layers

    for pkt in layers:
        if hasattr(pkt, "pid"):
            pid = pkt.pid if hasattr(pkt, 'pid') else 'N/A'
            cc = pkt.cc if hasattr(pkt, 'cc') else 'N/A'
            tsc = pkt.tsc if hasattr(pkt, 'tsc') else 'N/A'
            if tsc == '0x00000002':
                message = 'Scrambled with even key'
            elif tsc == '0x00000003':
                message = 'Scrambled with odd key'
            elif tsc == '0x00000000':
                message = 'Unscrambled'
            else:
                message = 'Unknown'

            result.append({
                "pid": pid,
                "cc": cc,
                "tsc": tsc,
                "message": message
            })
        if hasattr(pkt,"prog_map_pid")   :
            map_pid=pkt.prog_map_pid if hasattr(pkt, 'prog_map_pid') else 'N/A'
            map_num=pkt.prog_num if hasattr(pkt, 'prog_num') else 'N/A'
            result.append({
                "map_pid": map_pid,
                "map_num": map_num
            })
        if hasattr(pkt,"mpeg_pmt.stream.type")  :
            mpt_id=pkt._all_fields['mpeg_pmt.stream.elementary_pid'] if hasattr(pkt, 'mpeg_pmt.stream.elementary_pid') else 'N/A'
            mpt_type=pkt._all_fields['mpeg_pmt.stream.type'] if hasattr(pkt, 'mpeg_pmt.stream.type') else 'N/A'

            result.append({
                "Stream_id": mpt_id,
                "Stream_type": mpt_type

            })
            # print(mpt_id)
        if hasattr(pkt,"mpeg_descr.net_name.name"):
            nit_id=pkt._all_fields['mpeg_descr.net_name.name'] if hasattr(pkt, 'mpeg_descr.net_name.name') else 'N/A'
            result.append({
                "desc_name" :nit_id
            })


    return result

import subprocess
def process_ts_pcap(file : File):
    output_ts_file = file.file.path + ".ts"

    cap = pyshark.FileCapture(file.file.path)

    with open(output_ts_file, 'wb') as ts_file:
        for pack in cap:
            if 'UDP' in pack:
                udp_layer = pack['UDP']

                udp_payload = udp_layer.payload
                hex_string_without_colons = udp_payload.replace(":", "")

                byte_string = bytes.fromhex(hex_string_without_colons)
                ts_file.write(byte_string)



    infile = output_ts_file
    outfile = file.file.path + ".mp4"

    subprocess.run(['ffmpeg', '-i', infile, outfile])

    return {'success': True, 'message': 'TS file created successfully', 'video_file': file.file.url + ".mp4"}