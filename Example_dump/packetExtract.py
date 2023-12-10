import pyshark

pcap_file = 'Example_dump/sample.ts'

cap = pyshark.FileCapture(pcap_file)

for pack in cap:
    # check if the TS frame is an audio frame with PID = 0x01010
    if str(pack["MP2T"].PID) == '0x00000101':
        print(pack)
