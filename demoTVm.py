#!/usr/bin/python

import os
import subprocess
import time

# Transcode video file to suitable format

# Low resolution: QCIF (176x144, 30fps), QVGA (320x240, 30fps), HVGA (480x320, 30fps)
# 2 High resolution mode : TV(1280x720), TV (1920x1080), Frame rate, 15, 30, 60

in_video = "./video/bbb_1080p_30fps.mp4"
vcodec ="x264"
vform = "HVGA"

out_video = "./video/bbb_"+vcodec+"_"+vform+".mp4"

def transcode(in_video,out_video,codec,form):

	if codec == "x264":
		if form == "QCIF":		
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=176,height=144}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
				
		elif form == "QVGA":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=320,height=240}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
			
		elif form == "HVGA":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=480,height=320}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
		
		elif form == "HD720":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=1280,height=720}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
		
		elif form == "HD1080":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=1920,height=1080}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)


			
	elif codec == "mp4v":
		if form == "QCIF":		
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=176,height=144}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
		
		elif form == "QVGA":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=320,height=240}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
			
		elif form == "HVGA":
			command = "vlc -I dummy {} --sout=#'transcode{{acodec=none,scodec=none,vcodec={},fps=30,width=480,height=320}}:file{{mux=mp4,dst={}}}'".format(in_video,vcodec,out_video)
	
	return command

#cmd = transcode(in_video, out_video, vcodec, vform)
#os.system(cmd)

# Test for LR - Low Resolution sans TS, QCIF (176x144, 30fps), QVGA (320x240, 30fps), HVGA (480x320, 30fps)
# Tranmission over RTP using RTSP/SDP protocols. Two video codecs may be used H.264 et MP4
case = 0

if case == 0:
	# mode push RTP using RTSP without MPEG TS

	#start a server
	server="vlc {} --sout='#duplicate{{dst=display,dst=rtp{{dst=127.0.0.1,port=5004,sdp=file:///home/sofiene/MultiMedia/bbb.sdp}}}}' :sout-keep &".format(out_video)
	
	os.system(server)

	time.sleep(1)
	
	windowS = "wmctrl -r bbb_{}_{}.mp4 - Lecteur multimedia VLC -e 1,800,100,480,320".format(vcodec,vform)
	os.system(windowS)

	# start a client
	client = "vlc file:///home/sofiene/MultiMedia/bbb.sdp &"
	os.system(client)

	
	time.sleep(1)
	windowC = "wmctrl -r bbb.sdp - Lecteur multimedia -e 1,800,600,480,320"
	os.system(windowC)
	
	#call sondeTVm
	subprocess.call(["./sondeTVm.py", "LR"])

# Test for HR - High Resolution, HD720(1280x720), HD1080(1920x1080), Frame rate 30
# need to use MPEG TS over RTP for that case, 2 codec may be used H.264

elif case == 1 :

	# affichage local
	server = "vlc -I dummy {} --sout=\"#duplicate{{dst=rtp{{dst=127.0.0.1,port=5004,mux=ts,sap,name=SER}},dst=display}}\" --sout-keep &".format(out_video)

	os.system(server)

	time.sleep(5)

	windowS = "wmctrl -r Lecteur multimedia VLC -e 1,800,0,640,480"
	os.system(windowS)

	# start a client
	client = "vlc rtp://127.0.0.1:5004 &"

	os.system(client)
	time.sleep(5)

	windowC = "wmctrl -r rtp://127.0.0.1:5004 - Lecteur multimedia VLC -e 1,800,600,640,480"
	os.system(windowC)
	
	#call sondeTVm
	subprocess.call(["./sondeTVm.py", "HR"])

