from scapy.all import rdpcap, hexdump
import os
from dataclasses import dataclass
import socket


@dataclass
class packet_classifier_config:
    protocols = ["mpe", "ule", "sip", "rtp", "ftp", "sftp", "http", "https", "snmp", "pop", "smtp", "ssh"]

    parent_folder = "Classified packets"

    folders = []
    for protos in protocols:
        folders.append(os.path.join(parent_folder, protos))


    Protocol_dir = {}

    for i in range(len(protocols)):
        Protocol_dir[protocols[i]] = folders[i]

class packet_classifier:
    def __init__(self):
        '''
        Inherits packet_classifier_config and creates the folder stucture necessary for sorting the data packets 
        '''

        self.classifier_config = packet_classifier_config()

        try:
            # Create folders for classification
            self.makedir(self.classifier_config.parent_folder)

            for path in self.classifier_config.folders:
                self.makedir(path)

            print("directory created")

        except Exception as e:
            print("Folders not created", e)
    
    def makedir(self, path):
        '''
        Creates the dirctories only if they don't already exists
        '''
        if not os.path.exists(path):
            os.mkdir(path)

    def get_application_layer_packet(self, packet):
        '''
        returns the name of the application layer protocol of the given packet
        Input:
            packet: scapy packet to be decoded
        Output: 
            packet_name(str): name of the packet
        '''

        try:
            # look for the destination port number from tcp layer
            logical_port_number = packet.dport

            # find the protocol based on the destination port number
            protocol_name = socket.getservbyport(logical_port_number)
            if protocol_name not in self.classifier_config.protocols:
                raise Exception("Protocol out of scope or not valid")

            return protocol_name
        
        except Exception as e:

            return "UNKNOWN"
    
    def save_payload(self, packet):
        '''
        Save the payload in the dedicated folder
        Inputs:
            packet: scapy packet whose load is to be saved
        '''

        try:
            protocol_name = self.get_application_layer_packet(packet)

            if protocol_name != "UNKNOWN":

                folder_name = os.path.join(self.classifier_config.Protocol_dir[protocol_name], f"{packet.id}_{packet.seq}.txt")

                with open(folder_name, 'w') as file:
                    file.write(hexdump(packet, dump=True))
                file.close()
        
        except Exception as e:
           print("Couldn't Write payload to file", e)
                
            


if __name__ == "__main__":
    pc = packet_classifier()

    pkts = rdpcap("Media/temp.cap")
    for pkt in pkts:

        pc.save_payload(pkt)