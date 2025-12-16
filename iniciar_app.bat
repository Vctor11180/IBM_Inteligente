@echo off
echo ========================================
echo   NutriLife - Iniciar Aplicacion
echo ========================================
echo.

echo [1/2] Iniciando Backend...
start "NutriLife Backend" cmd /k "python backend/app.py"

echo.
echo Esperando 3 segundos para que el backend inicie...
timeout /t 3 /nobreak > nul

echo.
echo [2/2] Iniciando Frontend...
start "NutriLife Frontend" cmd /k "cd frontend && python -m http.server 8000"

echo.
echo ========================================
echo   Aplicacion iniciada!
echo ========================================
echo.
echo Backend: http://localhost:5000
echo Frontend: http://localhost:8000
echo.
echo Presiona cualquier tecla para cerrar esta ventana...
pause > nul

