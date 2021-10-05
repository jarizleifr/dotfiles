:: Setup HOME variable if not set
setx HOME %USERPROFILE%

set DOTFILES=%HOME%\dotfiles

:: Delete previous configs
rmdir %HOME%\.emacs.d

:: Create symbolic links for configurations in HOME
mklink /d %HOME%\.emacs.d %DOTFILES%\.emacs.d

:: Create startup links
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
robocopy "%DOTFILES%\startup" "%STARTUP%" /mir

