#!/usr/bin/python

import os
import sys
import csv
import time
import subprocess

case = sys.argv[1]

fieldnames = ["x_value", "mos"]

with open('mos_file.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	csv_writer.writeheader()

#start graphing process csv file and refresh parameter
os.system("chmod ogu+x ./qualityGraph/plot_mos_video.py")
os.system("./qualityGraph/plot_mos_video.py mos_file.csv 1000 &")

traceFile = "touch test.pcap"
os.system(traceFile)

rights = "chmod o=rw test.pcap"
os.system(rights)

for index in range(1, 3):
	probe = "sudo tshark  -i lo -f \"udp port 5004\" -F libpcap -a duration:10 -w test.pcap"
	os.system(probe)

	# extraire les informations globales
	if case == "LR":
		# rtsp avec sdp
		print "mode RTSP/SDP"
			
		# call model to calculate MOS
		subprocess.call(["./vmodel/simple_vmodel.py", str(index), "test.pcap", 'mos_file.csv'])	

	elif case == "HR":
		# rtp over mpeg ts 
		print "mode RTP"

		#call model to calculate MOS
		subprocess.call(["./vmodel/simple_vmodel.py", str(index), "test.pcap"])
