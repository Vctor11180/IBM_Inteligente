@echo off
echo ========================================
echo   NutriLife AI + Web3
echo   Iniciando Backend y Frontend
echo ========================================
echo.

REM Activar entorno virtual
echo [1/3] Activando entorno virtual...
call .venv\Scripts\activate.bat

REM Verificar que existe .env
if not exist backend\.env (
    echo.
    echo ❌ ERROR: No se encontró backend\.env
    echo.
    echo Por favor, crea el archivo backend\.env con:
    echo PINATA_JWT=tu_jwt_token_aqui
    echo.
    pause
    exit /b 1
)

echo [2/3] Iniciando Backend en http://localhost:5000
echo.
start "NutriLife Backend" cmd /k "cd /d %~dp0 && .venv\Scripts\activate.bat && python backend/app.py"

REM Esperar un poco para que el backend inicie
timeout /t 3 /nobreak >nul

echo [3/3] Iniciando Frontend en http://localhost:8000
echo.
start "NutriLife Frontend" cmd /k "cd /d %~dp0frontend && python -m http.server 8000"

echo.
echo ========================================
echo   ✅ Servicios iniciados
echo ========================================
echo.
echo   Backend:  http://localhost:5000
echo   Frontend: http://localhost:8000
echo.
echo   Presiona cualquier tecla para cerrar esta ventana...
echo   (Los servicios seguirán corriendo en otras ventanas)
echo.
pause >nul

