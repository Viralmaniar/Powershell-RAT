Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "C:\Python36\Mail.bat" & Chr(34), 0
Set WinScriptHost = Nothing