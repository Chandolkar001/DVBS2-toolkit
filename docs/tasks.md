### Backend Server
### BB Frame

- [ ] Study GSE header and payload
- [ ] Extract TS (stream/packetized) and GSE (stream/packetized) data from BB frames
- [ ] Generate dummy test data for all the input streams
- [ ] Find libraries and packages
- [ ] Categorize Continous and Packet data based on BB Header.

### Continous Data analyzer
- [ ] Convert to av format (.av, .mp4, etc) based on TS or GSE.
- [ ] store the data according to the type of media.
- [ ] If it is live-broadcasting, directly pass the feed to frontend using Django-channels

### Packet Data analyzer
- [ ] De-encapsulate based on GSE or TS.
- [ ] Use Scapy/ Pyshark to analyze and extract data from packets.
- [ ] Convert raw data to readable data.
- [ ] Categorize the raw data and store the data according to the type of media(image, video, audio, webpages, email, etc).
- [ ] API - Send packets to frontend.

### Storage 
- [ ] API - Access all the stored media and play it dynamically.


### Test cases generation 

- [ ] Use [dvbs2](https://github.com/igorauad/gr-dvbs2rx) to generate SDR based input test cases for MPEG-TS stream.
- [ ] Search for other GNU Radio - SDR based projects for dvbs2 test case generation 
