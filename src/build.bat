@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=popup_dictionary
set NAME=popup_dictionary
set PACKID=popup_dictionary
set VERSION=0.5.1-beta.1


quick_manifest.exe "%NAME%" "%PACKID%" >%REPO%\manifest.json

copy ..\LICENSE %REPO%


fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%\checksum.md5


cd %REPO%
%ZIP% ../%REPO%_v%VERSION%_CCBC.adze *
