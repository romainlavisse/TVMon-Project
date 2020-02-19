#!/usr/bin/python


import sys


case = sys.argv[1]

NombrPort = 0
ListRes = []
Video = False
text = open(case, "r")
Lines = text.readlines()


for line in Lines:
	if line != "\n":
		if  line.split()[0] == "m=video":
			Video = True
		
		if	line.split()[0] == "m=audio":
			Video = False


		if line.split(':')[0] == "a=rtpmap" and Video == True :
			VideoRTPPayloadType="videoRTPPayloadType "+line.split(':')[1].split()[0]
			Codec= "videoCodec "+line.split()[1].split('/')[0]
			ClockRate= "videoClockRate "+line.split()[1].split('/')[1]
	
				  
	
	

		if  line.split(':')[0]=="a=fmtp" and Video == True :
			PLI = line.split(';')[1]
	
	

			if PLI[21:23] == "0A" : #level 1.0
					FrameRate="videoFrameRate 15.0"
					Resolution="videoResolution QCIF"

			elif PLI[21:23] == "0B" : #level 1.1
					FrameRate="videoFrameRate 10.0"
					Resolution="videoResolution QVGA"

			elif PLI[21:23] == "0C": #level 1.2
					FrameRate="videoFrameRate 20.0"
					Resolution="videoResolution QVGA"

			elif PLI[21:23] == "0D": #level 1.3
				FrameRate="videoFrameRate 36.0"
				Resolution="videoResolution QVGA"

			elif PLI[21:23] == "14" : #level 2.0
				FrameRate="videoFrameRate 36.0"
				Resolution="videoResolution QVGA"
			elif PLI[21:23] == "15" : #level 2.1
				FrameRate="videoFrameRate 30.0"
				Resolution="videoResolution HVGA"

		elif line.split()[0] == "Transport:" :
			if line.split(';')[2].split('=')[0] == "client_port" :
				
				if  NombrPort == 0 :
					PortClient = "PortClient " + line.split(';')[2].split('=')[1].split('-')[0]
					NombrPort = 1

ListRes.append(Codec)
ListRes.append(ClockRate)
ListRes.append(VideoRTPPayloadType)
ListRes.append(FrameRate)
ListRes.append(Resolution)
ListRes.append(PortClient)


print(ListRes)
