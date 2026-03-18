@echo off
title AI API - Offline Runner

echo ======================================
echo     Starting AI API (Offline Mode)
echo ======================================

cd /d %~dp0

echo Starting executable...
start "" run_api.exe

echo Waiting for server to be ready...

:waitloop
timeout /t 2 >nul
curl -s http://127.0.0.1:8000/docs >nul 2>&1

if errorlevel 1 (
    echo Still loading model...
    goto waitloop
)

echo Server is ready!
start http://127.0.0.1:8000/docs

pause