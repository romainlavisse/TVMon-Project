from scapy.all import *
import pyshark,threading
import socket,binascii,re,matplotlib
filename_regex = re.compile(".*/(.*).sdp")
#print(socket.gethostbyname(socket.gethostname()))
#filename = "fulltest.pcap"
#pcapfile = rdpcap(filename)
current_client = {}
otime = round(time.time(),0)
client_time=[]
client_id=[]
video_history=[]

conf.iface="lo"
def sniffData(packet):
    cpt = 1
    for i in range(0,len(client_time)):
        if current_client.get(client_id[i]) != "":
            client_time[i][-1] =(client_time[i][-1][0],round(time.time() - otime,0) - client_time[i][-1][0])
     
    if (packet.haslayer(TCP)):
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
            if filename_regex.search(rtspstr) != None:
                current_client[packet[IP].src] = filename_regex.search(rtspstr).group(1)
                if packet[IP].src not in client_id :
                    client_id.append(packet[IP].src)
                    client_time.append([(round(time.time(),0)-otime,0)])
                    video_history.append([filename_regex.search(rtspstr).group(1)])
                else:
                    client_time[client_id.index(packet[IP].src)].append((round(time.time(),0)-otime,0))
                    video_history[client_id.index(packet[IP].src)].append(filename_regex.search(rtspstr).group(1))
                    
            else:
                return 
        if (len(packet[TCP])>20 and payload[0:16] == b"54454152444f574e"):
            if packet[IP].src in current_client.keys():
                current_client[packet[IP].src] = ""
                
    print(current_client)
    print(client_id)
    print(client_time)
    print(video_history)
sniff(prn=sniffData)


"""
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
        print(current_client)"""