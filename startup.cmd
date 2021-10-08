@echo off

:: 1. Browser
vdesk on:1 run:firefox -new-window "www.google.com"
timeout /t 5
:: 2. Code

vdesk on:2 run:emacsclientw -c -n -a runemacs
timeout /t 5

:: 3. Terminal
vdesk on:3 run:cmder
