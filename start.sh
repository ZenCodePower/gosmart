#!/bin/bash
# Script de démarrage du serveur GOSMART (LOCAL UNIQUEMENT)

# Port par défaut (peut être modifié via variable d'environnement PORT)
PORT=${PORT:-8001}

echo "🚀 Démarrage du serveur GOSMART en LOCAL..."
echo "📍 Le site sera accessible sur http://localhost:$PORT"
echo "⚠️  Modifications en LOCAL uniquement - PAS de déploiement automatique"
echo ""

cd "$(dirname "$0")"

# Activer l'environnement virtuel s'il existe
if [ -d "venv" ]; then
    echo "✅ Activation de l'environnement virtuel..."
    source venv/bin/activate
else
    echo "❌ Environnement virtuel non trouvé."
    echo ""
    echo "Créez-le avec une de ces méthodes :"
    echo "  Option 1 (UV - recommandé) : uv venv venv --python 3.11"
    echo "  Option 2 (Classique)        : python3 -m venv venv"
    echo ""
    echo "Puis installez les dépendances :"
    echo "  Avec UV  : uv pip install -r requirements.txt"
    echo "  Classique: pip install -r requirements.txt"
    exit 1
fi

# Démarrer le serveur avec rechargement automatique
echo "🔄 Serveur en mode --reload (rechargement automatique activé)"
echo "💡 Modifiez les fichiers et rafraîchissez votre navigateur pour voir les changements"
echo "🛑 Appuyez sur Ctrl+C pour arrêter le serveur"
echo ""
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port $PORT