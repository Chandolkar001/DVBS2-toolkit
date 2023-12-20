import pyshark
import os
import datetime
import json

class IPv4Parser:
    def __init__(self, hex_payload):
        self.hex_payload = hex_payload

    def parse(self):
        binary_payload = self.hex_to_binary()
        version = binary_payload[:4]
        header_length = int(binary_payload[4:8], 2) * 4  # in bytes
        ttl = int(binary_payload[32:40], 2)
        protocol = int(binary_payload[72:80], 2)
        # source_ip = '.'.join([str(int(binary_payload[i:i + 8], 2)) for i in range(96, 128, 8)])
        # destination_ip = '.'.join([str(int(binary_payload[i:i + 8], 2)) for i in range(128, 160, 8)])

        return {
            'version': version,
            'header_length': header_length,
            'ttl': ttl,
            'protocol': protocol,
            # 'source_ip': source_ip,
            # 'destination_ip': destination_ip,
            'remaining_payload': binary_payload[header_length * 8:]
        }

    def hex_to_binary(self):
        return bin(int(self.hex_payload, 16))[2:].zfill(len(self.hex_payload) * 4)

class UDPParser:
    def __init__(self, binary_payload):
        self.binary_payload = binary_payload

    def parse(self):
        source_port = int(self.binary_payload[:16], 2)
        destination_port = int(self.binary_payload[16:32], 2)
        length = int(self.binary_payload[32:48], 2)
        checksum = hex(int(self.binary_payload[48:64], 2))[2:]

        return {
            'source_port': source_port,
            'destination_port': destination_port,
            'length': length,
            'checksum': checksum,
            'remaining_payload': self.binary_payload[64:]
        }

class GREParser:
    def __init__(self, pcap_file_path):
        self.filter_str = 'ip.dst==192.168.0.31'
        self.cap = pyshark.FileCapture(pcap_file_path, display_filter=self.filter_str)
        self.S = '0'
        self.E = '0'
        self.Label_type = '00'
        self.GSE_length = '000'
        self.frag_id = '00'
        self.Total_length = '0000'
        self.Protocol_Type = '0000'
        self.Protocol_Table = {'0800': 'IPv4', '86dd': 'IPv6'}
        self.Label_Field = '000000000000'
        self.payload = '0'

    def test(self):
        print(f"S: {self.S}\nE: {self.E}\nLT: {self.Label_type}")
        print(f"GSE Length {self.GSE_length}")
        print(f"Protocol Type: {self.Protocol_Table[self.Protocol_Type]}")
        print(f"Label Field: {self.Label_Field}")
        print(f"Payload: {self.payload}")

    def parse_GSE(self):
        results = []
        i = 0
        for packet in self.cap:
            try:
                gse_frame = packet.udp.payload
                gse_frame = "".join(gse_frame.replace(":", ""))
                flags = self.hex_to_bin(gse_frame[0])
                self.S = flags[0]
                self.E = flags[1]
                self.Label_type = flags[2:]
                self.GSE_length = self.hex_to_bin(gse_frame[1:4])

                if self.S == '1' and self.E == '1':
                    self.frag_id = 'NOT APPLICABLE'
                    self.Total_length = 'NOT APPLICABLE'
                    self.Protocol_Type = gse_frame[4:8]
                    self.Label_Field = gse_frame[8:20]
                    self.payload = gse_frame[20:]

                     # IPv4 Parsing
                    ipv4_parser = IPv4Parser(self.payload)
                    ipv4_result = ipv4_parser.parse()

                    udp_parser = UDPParser(ipv4_result['remaining_payload'])
                    del ipv4_result['remaining_payload']
                    udp_result = udp_parser.parse()

                    result = {
                        'GSE': {
                            'S': self.S,
                            'E': self.E,
                            'Label_type': self.Label_type,
                            'GSE_length': self.GSE_length
                        },
                        'IPv4': ipv4_result,
                        'UDP': udp_result
                    }

                    results.append(result)
                else:
                    # Implement later
                    pass

            except Exception as e:
                print(e)
            except AttributeError:
                pass

        return results

    def hex_to_bin(self, hexstr):
        hex_integer = int(hexstr, 16)
        binary_string = bin(hex_integer)
        binary_string = binary_string[2:]
        return str(binary_string)

def getGSE(file):
    file_path = file.file.path
    parser = GREParser(file_path)
    return parser.parse_GSE()