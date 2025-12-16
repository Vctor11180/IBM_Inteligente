#!/bin/bash

echo "========================================"
echo "  NutriLife - Iniciar Aplicacion"
echo "========================================"
echo ""

echo "[1/2] Iniciando Backend..."
gnome-terminal -- bash -c "python backend/app.py; exec bash" 2>/dev/null || \
xterm -e "python backend/app.py" 2>/dev/null || \
python backend/app.py &

echo ""
echo "Esperando 3 segundos para que el backend inicie..."
sleep 3

echo ""
echo "[2/2] Iniciando Frontend..."
gnome-terminal -- bash -c "cd frontend && python -m http.server 8000; exec bash" 2>/dev/null || \
xterm -e "cd frontend && python -m http.server 8000" 2>/dev/null || \
(cd frontend && python -m http.server 8000) &

echo ""
echo "========================================"
echo "  Aplicacion iniciada!"
echo "========================================"
echo ""
echo "Backend: http://localhost:5000"
echo "Frontend: http://localhost:8000"
echo ""

