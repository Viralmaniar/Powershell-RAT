# Powershell-RAT
Python based backdoor that uses Gmail to exfiltrate data as an e-mail attachment. 

This RAT will help someone during red team engagements to backdoor any Windows machines. It tracks the user activity using screen capture and sends the information to an attacker as an e-mail attachment.

<B>Note: This piece of code is Fully UnDetectable (FUD) by Anti-Virus (AV) software. </B>

# Setup
- Throwaway Gmail email address
- Enable "Allow less secure apps" by going to https://myaccount.google.com/lesssecureapps
- Modify the `$username` & `$password` variable for your account in the Mail.ps1 poweshell file
- Modify `$msg.From` & `$msg.To.Add` with throwaway gmail address
