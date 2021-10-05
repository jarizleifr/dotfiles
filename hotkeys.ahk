#SingleInstance
#InstallKeybdHook

;; I use Ctrl-Ö to open Cmder, so Open Emacs with Ctrl-Ä
^ä::
Run, %scoop%\apps\emacs\current\bin\emacsclientw.exe -c -n -a %scoop%\apps\emacs\current\bin\runemacs.exe
return
	
;; Remap Capslock to act both as Control and Escape
SetCapsLockState, alwaysoff
Capslock::
Send {LControl Down}
KeyWait, CapsLock
Send {LControl Up}
if ( A_PriorKey = "CapsLock" )
{
  Send {Esc}
}
return