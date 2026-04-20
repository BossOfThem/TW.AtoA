@echo off
REM ============================================================
REM Ash to Altar — prototype launcher (data-driven mode)
REM ============================================================
REM Double-click this to serve prototype/ over http://localhost:8765/
REM and open the prototype in your default browser. This sidesteps
REM the file:// CORS block so prototype/data/*.json load at runtime.
REM
REM If you double-click index.html directly instead, the prototype
REM still plays — it falls back to inline defaults (see console).
REM ============================================================

cd /d "%~dp0"
start "" http://localhost:8765/index.html
py -m http.server 8765
