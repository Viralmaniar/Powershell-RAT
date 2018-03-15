# Powershell-RAT
Python based backdoor that uses Gmail to exfiltrate data as an e-mail attachment. 

This RAT will help someone during red team engagements to backdoor any Windows machines. It tracks the user activity using screen capture and sends the information to an attacker as an e-mail attachment.

<B>Note: This piece of code is Fully UnDetectable (FUD) by Anti-Virus (AV) software. </B>

# Setup
- Throwaway Gmail email address
- Enable "Allow less secure apps" by going to https://myaccount.google.com/lesssecureapps
- Modify the `$username` & `$password` variable for your account in the `Mail.ps1` Powershell file
- Modify `$msg.From` & `$msg.To.Add` with throwaway gmail address

# How do I use this?
- Press 1: This option sets the execution policy to unrestricted using `Set-ExecutionPolicy Unrestricted`. This is useful on administrator machine

- Press 2: This takes the screenshot of the current screen on the user machine using `Shoot.ps1` Powershell script

- Press 3: This option backdoors the user machine using `schtasks` and sets the task name to `MicrosoftAntiVirusCriticalUpdatesCore`

- Press 4: This option sends an email from the user machine using `Powershell`. These uses `Mail.ps1` file to send screenshot as attachment to exfiltrate data

- Press 5: This option backdoors the user machine using `schtasks` and sets the task name to `MicrosoftAntiVirusCriticalUpdatesUA`

- Press 6: This option deletes the screenshots from user machine to remain stealthy

- Press 7: This option backdoors the user machine using `schtasks` and sets the task name to `MicrosoftAntiVirusCriticalUpdatesDF`

- Press 8: This option performs all of the above with a single button `press 8` on a keyboard. Attacker will receive an email every `5 minutes` with screenshots as an email attachment. Screenshots will be deleted after `12 minutes`

- Press 9: Exit gracefully from the program or press `Contrl+C`

# To Do
- Get keyboard strokes
