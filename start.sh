#!/bin/bash
# Script de démarrage du serveur GOSMART

# Port par défaut (peut être modifié via variable d'environnement PORT)
PORT=${PORT:-8001}

echo "Démarrage du serveur GOSMART..."
echo "Le site sera accessible sur http://localhost:$PORT"
echo ""

cd "$(dirname "$0")"

# Activer l'environnement virtuel s'il existe
if [ -d "venv" ]; then
    echo "Activation de l'environnement virtuel..."
    source venv/bin/activate
fi

# Démarrer le serveur
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port $PORT