import pyshark
import os

# Classified packets -> pcap_name -> http -> ip.id

class CategorizePcap:
    def __init__(self):
        self.parent_folder = "Classified Packets"
        self.makedir(self.parent_folder)
        self.proto_names = []

        self.PAYLOAD_LAYER_NUMBER = 3
        self.APPLICATION_LAYER_NUMBER = -1
    
    def makedir(self, path):
        '''
        Creates the dirctories only if they don't already exists
        '''
        if not os.path.exists(path):
            os.mkdir(path)

    def get_protocol_layer(self, packet):
        names = [x.layer_name for x in packet.layers]
        if len(names) > 1:
            return names[self.APPLICATION_LAYER_NUMBER]
        else:
            return None
        
    def get_pcap_name(self, pcap_file_path):
        file_name, file_extension = os.path.splitext(os.path.basename(pcap_file_path))
        return file_name
    
    def get_byte_array(self, payload):
        raw_data = bytearray.fromhex(payload.replace(":",""))
        return raw_data


    def process_pcap(self, pcap_file_path):
        cap = pyshark.FileCapture(pcap_file_path)
        pcap_file_path = os.path.join(self.parent_folder, self.get_pcap_name(pcap_file_path))
        for packet in cap:
            try:
                protocol_name = self.get_protocol_layer(packet)
                if protocol_name:                    
                    # print(protocol_name)
                    self.makedir(pcap_file_path)
                    
                    protocol_file_path = os.path.join(pcap_file_path, protocol_name)

                    if protocol_name not in self.proto_names:
                        self.makedir(protocol_file_path)
                        self.proto_names.append(protocol_name)

                    payload_file_path = os.path.join(protocol_file_path, f"{packet.ip.id}.txt")

                    with open(payload_file_path, 'ab') as file:
                        file.write(self.get_byte_array(packet[self.PAYLOAD_LAYER_NUMBER].payload))
                        print("writing done")


            except Exception as e:
                print("Processing Failed")
                print(e)


if __name__ == "__main__":
    cp = CategorizePcap()
    input_path = "Media/tshtml.ts"
    cp.process_pcap(input_path)
