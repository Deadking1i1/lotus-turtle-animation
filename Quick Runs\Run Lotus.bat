@echo off
cd /d "%~dp0.."
py -3 Lotus.py
if errorlevel 1 python Lotus.py
