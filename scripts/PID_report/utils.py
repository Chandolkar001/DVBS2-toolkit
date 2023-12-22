import pyshark

pid_description_dict = {
    '0x00000000': "PAT",
    '0x00000001': "CAT",
    '0x00000002': "TSDT",
    '0x00000003': "IPMP table",
    '0x00000004': "Reserved",
    '0x0000000f': "Reserved",
    '0x00000010': "NIT, ST",
    '0x00000011': "SDT, BAT, ST",
    '0x00000012': "EIT, ST, CIT",
    '0x00000013': "RST, ST",
    '0x00000014': "TDT, TOT, ST",
    '0x00000015': "network synchronization",
    '0x00000016': "RNT",
    '0x00000017': "Reserved for future use",
    '0x0000001b': "Reserved for future use",
    '0x0000001c': "inband signalling",
    '0x0000001d': "measurement",
    '0x0000001e': "DIT",
    '0x0000001f': "SIT",
    '0x00001ffb': "DigiCipher 2/ATSC MGT metadata",
    '0x00001ffc': "PMT reserved",
    '0x00001ffe': "PMT reserved",
    '0x00001fff': "Null Packet",
    '0x00000021' : "MPEG - Video",
    '0x00000020' : "MPEG - Audio",

}

def calculate_bitrate(packet_count, duration):
    total_bits = sum(int(packet.length) * 8 for packet in packet_count)
    bitrate = total_bits / duration
    return bitrate

def PID_analysis(capture_file):
    shark_cap = pyshark.FileCapture(capture_file)

    packet_count = list(shark_cap)
    bitrate = calculate_bitrate(packet_count, 10)

    pid_to_data = dict()

    for shark in shark_cap:
        for i in range(len(shark.layers)):
            if shark.layers[i].layer_name == 'mp2t':
                sec_pid = shark.layers[i].PID
    
                if not sec_pid in pid_to_data and sec_pid in pid_description_dict:
                    hex_v = sec_pid.hex_value
                    sec_pid = str(sec_pid)
                    pid_to_data[sec_pid] = [1, pid_description_dict[sec_pid], hex_v, bitrate]
                elif sec_pid in pid_to_data and sec_pid in pid_description_dict:
                    pid_to_data[sec_pid][0] += 1

    return pid_to_data
