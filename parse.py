from scapy.all import *
import socket,binascii,re,matplotlib
filename_regex = re.compile(".*/(.*).sdp")
print(socket.gethostbyname(socket.gethostname()))
filename = "fulltest.pcap"
pcapfile = rdpcap(filename)
current_client = {}
for packet in pcapfile:
    if (packet.haslayer(TCP) and packet[IP].src != socket.gethostbyname(socket.gethostname())):
        payload = binascii.hexlify(bytes(packet[TCP].payload))
        if (len(packet[TCP])>20 and payload[0:14] == b"4f5054494f4e53"):
            endrtsp = 0
            rtspstr = ""
            for i in range(16,len(packet[TCP]),2):
                if payload[i:i+2] == b"20":
                    endrtsp = i
                    break
                else:
                    rtspstr+=chr(int(payload[i:i+2],16))

            current_client[packet[IP].src] = filename_regex.search(rtspstr).group(1)
        if (len(packet[TCP])>20 and payload[0:16] == b"54454152444f574e"):
            if packet[IP].src in current_client.keys():
                del current_client[packet[IP].src]
        print(current_client)