@echo off

REM Check if Python is installed
python --version 2>NUL
IF NOT %ERRORLEVEL% == 0 (
    echo Python is not installed. Installing Python...
    
    REM Download the latest Python installer
    powershell -Command "& {$PythonInstallerUrl = 'https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe'; Invoke-WebRequest $PythonInstallerUrl -OutFile 'python-installer.exe'}"
    
    REM Install Python
    python-installer.exe /quiet PrependPath=1
    
    REM Clean up the installer
    del python-installer.exe
    
    echo Python has been installed.
)

REM Run the Python file
python scrape_smasaga.py
