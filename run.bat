@echo off



echo.
echo #################################################
echo CPYTHON:
C:/Python27/python.exe main.py

echo.
echo #################################################
echo PYPY:
C:/Users/madig/Downloads/pypy2.7-v7.3.20-win64/pypy2.7-v7.3.20-win64/pypy.exe main.py

echo.
echo #################################################
echo IRONPYTHON:
"C:/Program Files/IronPython 2.7/ipy.exe" main.py

echo.
echo #################################################
echo JYTHON:
java -jar "C:\Users\madig\Downloads\jython2.7.4\jython.jar" main.py