@echo off & cls
title Run Roblox Gen
set /p action= Install Requirements (y/n):
if '%action%'=='y' goto requests
of '%action%'=='n' goto start

:requirements
title Installing Requirements
python -m pip install requests
start


:start
python main.py
pause
