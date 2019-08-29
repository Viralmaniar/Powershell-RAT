# Powershell-RAT
Python based backdoor that uses Gmail to exfiltrate data as an e-mail attachment. 

This RAT will help someone during red team engagements to backdoor any Windows machines. It tracks the user activity using screen capture and sends the information to an attacker as an e-mail attachment.

<B>Note: This piece of code is Fully UnDetectable (FUD) by Anti-Virus (AV) software. </B>

<B><I>This project must not be used for illegal purposes or for hacking into system where you do not have permission, it is strictly for educational purposes and for people to experiment with.</I></B>

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# RAT Architecture Diagram

![image](https://user-images.githubusercontent.com/3501170/54605214-dd51f400-4a9c-11e9-8b51-a225b13ecd0d.png)


# Screenshot
On the first run of the `Powershell-RAT` user will get options as below:

![image](https://user-images.githubusercontent.com/3501170/37453784-e926b64a-288c-11e8-9c8d-abaaf1b7dd3d.png)

Using `Hail Mary` option to backdoor a Windows machine:

![image](https://user-images.githubusercontent.com/3501170/37453816-fdfffaea-288c-11e8-9a60-0adcd0dc4599.png)

Successfully taking screenshots of the user activity:

![image](https://user-images.githubusercontent.com/3501170/37453833-0c7f3e78-288d-11e8-969e-5499cf53f2fd.png)

Data exfiltrated as an email attachment using Gmail:

![image](https://user-images.githubusercontent.com/3501170/37453864-233384d0-288d-11e8-8699-e5dbe149925c.png)

# My Windows machine do not have Python installed, what should I do?

- Compile `PowershellRAT.py` into an executable using [Pyinstaller](https://github.com/pyinstaller/pyinstaller)

- PyInstaller is available on PyPI. You can install it through pip:

<pre>
pip install pyinstaller
</pre>

# Setup
- Throwaway Gmail address
- Enable "Allow less secure apps" by going to https://myaccount.google.com/lesssecureapps
- Modify the `$username` & `$password` variables for your account in the `Mail.ps1` Powershell file
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

- Press 9: Exit gracefully from the program or press `Control+C`

# Questions?

Twitter: https://twitter.com/maniarviral
LinkedIn: https://au.linkedin.com/in/viralmaniar

# Contribution & License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.</br>
Want to contribute? Please fork it and hit up with a pull request.

Any suggestions or ideas for this tool are welcome - just tweet me on [@ManiarViral](https://twitter.com/maniarviral)

# To Do
- Encrypted exfil over Gmail to defeat SSL inspection
- Get photos from front camera
- Record mic
