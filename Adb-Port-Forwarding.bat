echo off
color f
cd adb
title Adb-Port-Forwarding
adb forward tcp:8080 tcp:8080
mode con: cols=50 lines=5
cls
echo.
echo Forwarding Phone Port:8080 To Pc Port:8080
echo.
set /p "op="