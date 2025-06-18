@echo off
REM Set the title of the terminal
title Start MyPortfolio Application

REM Navigate to the project directory
cd /d "%~dp0"

REM Check if Redis is running
echo Checking if Redis is running...
redis-cli ping >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Redis is not running. Starting Redis server...
    start "" "C:\path\to\redis-server.exe"
    timeout /t 5 >nul
) else (
    echo Redis is already running.
)

REM Activate the Python virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Start the FastAPI server
echo Starting FastAPI server...
uvicorn main:app --reload

REM Keep the terminal open after the server exits
pause