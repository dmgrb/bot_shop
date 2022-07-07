@echo off

call %~dp0/venv/Scripts/activate
cd %~dp0/

set TOKEN=

python bot1.py

pause