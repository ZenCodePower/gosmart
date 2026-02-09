# GOSMART - Site Web de Présentation

Site web professionnel pour présenter l'invention GOSMART - Support Smartphone Multi-Orientable avec système de facettes breveté.

## 🚀 Démarrage rapide

### Pour Cloner le Projet (Nouvel Ordinateur)

```bash
# 1. Cloner le projet depuis GitHub
git clone https://github.com/ZenCodePower/gosmart.git
cd gosmart

# 2. Créer l'environnement virtuel
python3 -m venv venv

# 3. Activer l'environnement et installer les dépendances
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
pip install -r requirements.txt

# 4. Démarrer le serveur
./start.sh
```

### Pour un Projet Déjà Cloné

```bash
# 1. Activer l'environnement virtuel
source venv/bin/activate  # Sur Windows : venv\Scripts\activate

# 2. Démarrer le serveur
./start.sh
```

Le site sera accessible sur **http://localhost:8001** (ou 8002 si 8001 est occupé)

> 📖 **Guides détaillés** :
> - `GUIDE_CLONAGE.md` - Guide complet de clonage
> - `INSTRUCTIONS_SIMPLES.md` - Pour débutants absolus
> - `TESTER_LOCAL.md` - Tester sans déployer

## 📁 Structure du Projet

```
JM/
├── backend/
│   └── main.py                 # Application FastAPI
├── frontend/
│   ├── templates/
│   │   ├── index.html          # Page d'accueil
│   │   ├── products.html       # Page produits/galerie
│   │   ├── about.html          # Page à propos de l'inventeur
│   │   └── contact.html        # Page contact
│   └── static/
│       ├── css/
│       │   └── style.css       # Styles CSS modernes
│       ├── js/
│       │   └── main.js         # JavaScript interactions
│       └── media/              # Photos et vidéos
├── video&photos/               # Sources des médias
├── requirements.txt            # Dépendances Python
├── contacts.json               # Stockage des contacts
├── start.sh                    # Script de démarrage
└── README.md
```

## 🎨 Pages du site

### 1. Accueil (`/`)
- Hero section avec image des modèles
- Vidéo de démonstration
- Avantages clés du GOSMART
- Cas d'usage (petit-déjeuner, rasage)
- Aperçu de la galerie
- Spécifications techniques

### 2. Produits (`/products`)
- Vue d'ensemble de tous les modèles
- Galerie modèle Vintage (téléphone d'antan)
- Galerie modèle Original
- Photos avec smartphone
- Section prototypes R&D

### 3. À propos (`/about`)
- Photo et bio de l'inventeur (Jean-Michel Didier)
- Parcours : Ingénieur Centrale Paris
- Caractère innovant de l'invention
- Participation au Concours Lépine 2026

### 4. Contact (`/contact`)
- Formulaire de contact avec sujets
- Types de collaboration recherchés
- FAQ

## ✨ Fonctionnalités

- ✅ Design moderne, professionnel et "tape-à-l'oeil"
- ✅ Support multilingue (Français / Anglais)
- ✅ Formulaire de contact avec sauvegarde
- ✅ Galerie d'images avec lightbox
- ✅ Vidéo de démonstration
- ✅ Responsive (mobile/tablette/desktop)
- ✅ Animations au scroll
- ✅ Navigation fixe avec effet de scroll

## 🔗 API Endpoints

- `GET /` - Page d'accueil
- `GET /products` - Page produits
- `GET /about` - Page à propos
- `GET /contact` - Page contact
- `POST /api/contact` - Soumission formulaire
- `GET /api/contacts` - Liste des contacts (admin)
- `GET /api/stats` - Statistiques contacts

## 📧 Gestion des contacts

Les messages sont sauvegardés dans `contacts.json` avec :
- Nom, email, message
- Sujet (info, partnership, patent, press, other)
- Préférence newsletter
- Langue et timestamp

## 🎯 Prochaines étapes

Pour mettre le site en production (gosmart.com) :

1. **Hébergement** : Déployer sur un serveur (Render, Railway, DigitalOcean, OVH...)
2. **Domaine** : Acheter gosmart.com et configurer DNS
3. **HTTPS** : Configurer SSL/TLS
4. **Base de données** : Migrer contacts.json vers PostgreSQL/MongoDB
5. **SEO** : 
   - Ajouter sitemap.xml
   - Optimiser meta tags
   - Soumettre à Google Search Console
6. **Analytics** : Intégrer Google Analytics / Plausible

## 🔧 Personnalisation

### Modifier les couleurs
Éditez les variables CSS dans `frontend/static/css/style.css` :

```css
:root {
    --accent: #ff6b35;        /* Couleur principale */
    --primary: #0a0a0a;       /* Fond sombre */
    --secondary: #141414;     /* Fond secondaire */
}
```

### Ajouter un lien vers le brevet
Modifiez le lien `#patent-link` dans `index.html` pour pointer vers votre document de brevet.

## 📝 Notes

- Le site fonctionne en local, prêt pour la mise en production
- Les images sont optimisées pour le web
- Le design s'inspire de vexub.fr avec une esthétique tech moderne

---

**GOSMART** - Support Smartphone Multi-Orientable  
*Brevet déposé - Jean-Michel Didier*  
*Concours Lépine International Paris 2026*
