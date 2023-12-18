import pyshark
from pydub import AudioSegment
import io

def create_raw_audio_file():
    cap = pyshark.FileCapture("VOIP.pcap", display_filter="udp")

    rtp_load_list = []

    print("starting pcap processing")

    for pkts in cap:
        try:
            rtp_packet = pkts[6]
            if rtp_packet.payload:
                rtp_load_list.append(rtp_packet.payload.split(":"))

        except:
            pass
    with open("rawaudio.bin", 'wb') as file:
        for rtp_packet in rtp_load_list:
            packet = " ".join(rtp_packet)
            bytepacket = bytearray.fromhex(packet)
            file.write(bytepacket)
    
    print("done")

def extract_audio(rtp_payload):
    print("Converting hex to audio")
    extracted_audio = AudioSegment.silent()

    for rtp_packet in rtp_payload:
        packet = " ".join(rtp_packet)
        bytepacket = bytearray.fromhex(packet)

        audio = AudioSegment(bytepacket, sample_width=2, frame_rate=8000, channels=1)
        if audio:
            extracted_audio += audio
    
    print("Converted")
    return extracted_audio

def process_pcap(pcap_file_path):
    cap = pyshark.FileCapture("VOIP.pcap", display_filter="udp")

    rtp_load_list = []

    print("starting pcap processing")

    for pkts in cap:
        try:
            rtp_packet = pkts[6]
            if rtp_packet.payload:
                rtp_load_list.append(rtp_packet.payload.split(":"))

        except:
            pass

    print(rtp_load_list[0])
    print("finished")

    return extract_audio(rtp_load_list)

def export_audio(audio, output_file_path):
    print("exporting ....")
    audio.export(output_file_path, format="wav")
    print("exported!")
    


if __name__ == "__main__":
    # pcap_file_path = "VOIP.pcap"
    # output_file_path = "call.wav"

    # raw_audio_file = process_pcap(pcap_file_path)
    # export_audio(raw_audio_file, output_file_path)

    create_raw_audio_file()

'''
udp_list = []
cap = pyshark.FileCapture('VOIP.pcap', display_filter='udp')
print("started writing to result.raw")
for i in cap:
    try:
        udp = i[6]
        if udp.payload:
             udp_list.append(udp.payload.split(":"))
    except:
        pass
print("finished extracting")

extracted_audio = AudioSegment.silent()
for rtp_packet in udp_list:
    packet = " ".join(rtp_packet)
    audio = bytearray.fromhex(packet)
    
print("finished writing")
'''
