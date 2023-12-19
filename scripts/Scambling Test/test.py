# import pyshark


# pcap_file = 'D:\PICT\SIH\SIH23-DVBS2\scripts\Scambling Test\sih_sample1.pcap'
# number= 14
# cap = pyshark.FileCapture(pcap_file)
# for pack in cap:
#     print(pack.MP2T.pid)
# # count =0
# # for pack in cap:
# #     # check if the TS frame is an audio frame with PID = 0x01010
# #     if str(pack["MP2T"].tsc) == '0x00000002':
# #         count=count+1
    
# # #     print(count)
# # for i in range(3,12):
# #     # dict={cap[number][i].cc:cap[number][i].tsc}
# #     print(cap[number][i])

# # print(cap[number][10]._all_fields)


import pyshark

pcap_file = 'D:\PICT\SIH\SIH23-DVBS2\scripts\Scambling Test\sih_sample1.pcap'
pid_set = set()

cap = pyshark.FileCapture(pcap_file)
for pack in cap:
    try:
        pid_value = pack.MP2T.pid  # Convert PID value from hexadecimal to integer
        tag=0x65
        if (pack.mpeg_descr.tag == tag):

            print(pack.mpeg_descr.tag)
            # print("break",end='\n')
            # break
        
        pid_set.add(pid_value)
    except AttributeError:
        print("No PID found for packet:")

print("Unique PIDs in the pcap file:", pid_set)
