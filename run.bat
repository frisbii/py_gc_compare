@echo off
setlocal enabledelayedexpansion

REM https://www.python.org/downloads/release/python-2718/
REM https://pypy.org/download.html
REM https://www.jython.org/download.html
REM https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.12

for /f "tokens=1,2 delims==" %%A in (config.ini) do (
    set "line=%%A"
    set "value=%%B"
    if "!line!"=="CPY_PATH" set "CPY_PATH=!value!"
    if "!line!"=="PYPY_PATH" set "PYPY_PATH=!value!"
    if "!line!"=="IPY_PATH" set "IPY_PATH=!value!"
    if "!line!"=="JY_PATH" set "JY_PATH=!value!"
)

echo.
echo #################################################
echo CPYTHON:

%CPY_PATH% main.py

echo.
echo #################################################
echo PYPY:
%PYPY_PATH% main.py

echo.
echo #################################################
echo IRONPYTHON:
%IPY_PATH% main.py

echo.
echo #################################################
echo JYTHON:
java -jar %JY_PATH% main.py