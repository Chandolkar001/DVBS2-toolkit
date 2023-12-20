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


keys_psi = ['pat', 'pmt', 'nit', 'cat']
PSI_info = dict.fromkeys(keys_psi)
# si info table
keys_si = ['SDT', 'EIT', 'TOT']
SI_info = dict.fromkeys(keys_si)
# PSISI info
keys_psisi = ['psi_info', 'si_info']
PSISI = dict.fromkeys(keys_psisi)

def PID_analysis(file):
    capture_file = file.file.path
    shark_cap = pyshark.FileCapture(capture_file)
    # print(shark_cap[1093].layers)
    # print(shark_cap[447].layers)

    for shark in shark_cap:
        for i in range(len(shark.layers)):
            if shark.layers[i].layer_name == 'mpeg_pmt':
               if PSI_info['pmt'] is not None:
                    PSI_info['pmt'].append(shark.layers[i]._all_fields)
               else:
                    PSI_info['pmt'] = [shark.layers[i]._all_fields]
            elif shark.layers[i].layer_name == 'mpeg_pat':
               if PSI_info['pat'] is not None:
                    PSI_info['pat'].append(shark.layers[i]._all_fields)
               else:
                    PSI_info['pat'] = [shark.layers[i]._all_fields] 
            elif shark.layers[i].layer_name == 'dvb_nit':
               if PSI_info['nit'] is not None:
                    PSI_info['nit'].append(shark.layers[i]._all_fields)
               else:
                    PSI_info['nit'] = [shark.layers[i]._all_fields] 
            elif shark.layers[i].layer_name == 'dvb_sdt':
               if SI_info['SDT'] is not None:
                    SI_info['SDT'].append(shark.layers[i]._all_fields)
               else:
                    SI_info['SDT'] = [shark.layers[i]._all_fields] 
            elif shark.layers[i].layer_name == 'dvb_eit':
               if SI_info['EIT'] is not None:
                    SI_info['EIT'].append(shark.layers[i]._all_fields)
               else:
                    SI_info['EIT'] = [shark.layers[i]._all_fields] 
            elif shark.layers[i].layer_name == 'mpeg_ca':
               if PSI_info['cat'] is not None:
                    PSI_info['cat'].append(shark.layers[i]._all_fields)
               else:
                    PSI_info['cat'] = [shark.layers[i]._all_fields] 
            
    unique_set_pmt = {frozenset(d.items()) for d in PSI_info['pmt']}
    PSI_info['pmt'] = [dict(fs) for fs in unique_set_pmt]

    unique_set_pat = {frozenset(d.items()) for d in PSI_info['pat']}
    PSI_info['pat'] = [dict(fs) for fs in unique_set_pat]

    unique_set_nit = {frozenset(d.items()) for d in PSI_info['nit']}
    PSI_info['nit'] = [dict(fs) for fs in unique_set_nit]

    unique_set_sdt = {frozenset(d.items()) for d in SI_info['SDT']}
    SI_info['SDT'] = [dict(fs) for fs in unique_set_sdt]

    unique_set_eit = {frozenset(d.items()) for d in SI_info['EIT']}
    SI_info['EIT'] = [dict(fs) for fs in unique_set_eit]

    unique_set_cat = {frozenset(d.items()) for d in PSI_info['cat']}
    PSI_info['cat'] = [dict(fs) for fs in unique_set_cat]


    PSISI['psi_info'] = PSI_info
    PSISI['si_info'] = SI_info

    return PSISI

import uuid

def multiple_video_extract(file):
    input_file = file.file.path
    output_ts_file = file.file.path + '.ts'

    

    cap = pyshark.FileCapture(input_file)

    with open(output_ts_file, 'wb') as ts_file:
        for pack in cap:
            if 'UDP' in pack:
                udp_layer = pack['UDP']

                udp_payload = udp_layer.payload
                hex_string_without_colons = udp_payload.replace(":", "")

                byte_string = bytes.fromhex(hex_string_without_colons)
                ts_file.write(byte_string)

    input_file = output_ts_file  # ts file as input

    max_j = 5
    output_prefix = "out"
    file_list = []
    for j in range(0, max_j + 1):

        mp4_output_file = f'{output_prefix}{j}.mp4'
        mp4_command = [
            'ffmpeg',
            '-y',
            '-i', input_file,
            '-map', f'0:v:{j-1}',
            mp4_output_file
        ]

        try:
            subprocess.run(mp4_command, check=True)
            print(f'Conversion to {mp4_output_file} successful!')
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')


        wav_output_file = f'{output_prefix}{j}.wav'
        wav_command = [
            'ffmpeg',
            '-y',
            '-i', input_file,
            '-map', f'0:a:{j-1}',
            wav_output_file
        ]

        try:
            subprocess.run(wav_command, check=True)
            print(f'Conversion to {wav_output_file} successful!')
        except subprocess.CalledProcessError as e:
            print(f'Error: {e}')

        # final_output_file = os.path.join(output_directory, f'final{j}.mp4')
        final_output_file = file.file.path + f'_final{j}.mp4'

        combine_command = [
            'ffmpeg',
            '-i', mp4_output_file,
            '-i', wav_output_file,
            '-c:v', 'copy',
            '-c:a', 'aac',
            final_output_file
        ]
        file_list.append(file.file.url + f'_final{j}.mp4')

        try:
            subprocess.run(combine_command, check=True)
            print(f'Combining {mp4_output_file} and {wav_output_file} into {final_output_file} successful!')
        except subprocess.CalledProcessError as e:
            file_list.remove(file.file.url + f'_final{j}.mp4')
            print(f'Error: {e}')

        try:
            os.remove(wav_output_file)
        except:
            pass

    return {"video_files" : file_list}
