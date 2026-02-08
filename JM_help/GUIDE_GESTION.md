# 📚 Guide de Gestion du Site GOSMART

Guide complet pour gérer, modifier et mettre à jour le site web GOSMART.

---

## 📁 Structure du Projet

```
JM/
├── backend/
│   └── main.py              # Logique serveur (FastAPI)
├── frontend/
│   ├── templates/           # Pages HTML
│   │   ├── index.html       # Page d'accueil
│   │   ├── products.html    # Page produits
│   │   ├── about.html       # Page à propos
│   │   └── contact.html     # Page contact
│   └── static/              # Fichiers statiques
│       ├── css/
│       │   └── style.css    # Styles du site
│       ├── js/
│       │   └── main.js      # JavaScript
│       └── media/           # ⭐ PHOTOS ET VIDÉOS ICI
│           ├── autostable/
│           ├── coque/
│           ├── handle/
│           ├── mini/
│           ├── mural/
│           ├── prototypes/
│           └── brevet/
└── video&photos/           # Dossier source des médias
```

---

## 🖼️ Comment Ajouter des Photos et Vidéos

### Étape 1 : Préparer vos fichiers

1. **Photos** : Format recommandé `.jpeg` ou `.jpg`
   - Résolution : minimum 1920x1080 pixels
   - Taille : idéalement < 2 MB par image
   - Nommez-les clairement : `photo-autostable-1.jpeg`

2. **Vidéos** : Format recommandé `.mp4` ou `.MOV`
   - Taille : idéalement < 50 MB (sinon utiliser Git LFS)
   - Nommez-les clairement : `demo-gosmart.mp4`

### Étape 2 : Copier les fichiers

**Option A - Via le terminal (Mac/Linux) :**

```bash
# 1. Aller dans le dossier du projet
cd /Users/fayerart/Documents/perso/JM

# 2. Copier une photo dans un dossier existant
cp "chemin/vers/votre-photo.jpeg" frontend/static/media/autostable/

# 3. Ou créer un nouveau dossier
mkdir -p frontend/static/media/nouveau-modele
cp "chemin/vers/votre-photo.jpeg" frontend/static/media/nouveau-modele/
```

**Option B - Via l'explorateur de fichiers :**

1. Ouvrez le dossier : `JM/frontend/static/media/`
2. Glissez-déposez vos fichiers dans le bon sous-dossier
3. Organisez par modèle (autostable, coque, handle, etc.)

### Étape 3 : Utiliser les fichiers dans le site

Une fois copiés, utilisez-les dans les pages HTML avec le chemin :

```html
<img src="/static/media/nom-dossier/nom-fichier.jpeg" alt="Description">
```

**Exemple :**
```html
<img src="/static/media/autostable/IMG_0566.jpeg" alt="GOSMART Autostable">
```

---

## 📄 Comment Modifier une Page Existante

### Modifier le contenu texte

1. **Ouvrez le fichier HTML** dans `frontend/templates/`
   - `index.html` = Page d'accueil
   - `products.html` = Page produits
   - `about.html` = Page à propos
   - `contact.html` = Page contact

2. **Trouvez le texte à modifier**

Les textes ont des attributs `data-fr` et `data-en` pour le multilingue :

```html
<h2 data-fr="Titre en français" data-en="Title in English">Titre en français</h2>
```

**Pour modifier :**
- Changez le texte entre les balises `<h2>...</h2>`
- Changez aussi `data-fr="..."` pour le français
- Changez aussi `data-en="..."` pour l'anglais

### Modifier une image

**Trouvez la ligne avec l'image :**
```html
<img src="/static/media/autostable/IMG_0566.jpeg" alt="Description">
```

**Remplacez par votre nouvelle image :**
```html
<img src="/static/media/autostable/votre-nouvelle-photo.jpeg" alt="Description">
```

### Modifier une vidéo

**Trouvez la section vidéo :**
```html
<video id="demo-video" controls>
    <source src="/static/media/IMG_0940.MOV" type="video/quicktime">
</video>
```

**Remplacez le nom du fichier :**
```html
<source src="/static/media/votre-nouvelle-video.mp4" type="video/mp4">
```

---

## ➕ Comment Ajouter une Nouvelle Page

### Étape 1 : Créer le fichier HTML

1. Créez un nouveau fichier dans `frontend/templates/`
   - Exemple : `nouvelle-page.html`

2. **Copiez la structure de base** depuis une page existante :

```html
<!DOCTYPE html>
<html lang="fr" id="html-root">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title data-fr="Titre | GOSMART" data-en="Title | GOSMART">Titre | GOSMART</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <!-- Navigation (copiez depuis index.html) -->
    <nav class="navbar scrolled" id="navbar">
        <!-- ... -->
    </nav>

    <!-- Votre contenu ici -->
    <section style="padding: 180px 0 80px;">
        <div class="container">
            <h1>Votre contenu</h1>
        </div>
    </section>

    <!-- Footer (copiez depuis index.html) -->
    <footer class="footer">
        <!-- ... -->
    </footer>

    <script src="/static/js/main.js"></script>
</body>
</html>
```

### Étape 2 : Ajouter la route dans le backend

Ouvrez `backend/main.py` et ajoutez :

```python
@app.get("/nouvelle-page", response_class=HTMLResponse)
async def nouvelle_page(request: Request):
    """Nouvelle page"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("nouvelle-page.html", {"request": request, "lang": lang})
```

### Étape 3 : Ajouter le lien dans le menu

Dans tous les fichiers HTML (`index.html`, `products.html`, etc.), ajoutez dans la navigation :

```html
<li><a href="/nouvelle-page" data-fr="Nouvelle Page" data-en="New Page">Nouvelle Page</a></li>
```

---

## 🎨 Comment Modifier le Design (Couleurs, Styles)

### Modifier les couleurs principales

1. Ouvrez `frontend/static/css/style.css`

2. Trouvez la section `:root` au début du fichier :

```css
:root {
    --primary: #0a0a0a;        /* Fond principal (noir) */
    --secondary: #141414;      /* Fond secondaire */
    --accent: #ff6b35;         /* Couleur d'accent (orange) */
    --accent-light: #ff8c5a;   /* Orange clair */
    --text-primary: #ffffff;   /* Texte principal (blanc) */
    --text-secondary: #a0a0a0; /* Texte secondaire (gris) */
}
```

3. **Changez les valeurs** pour vos couleurs préférées :

```css
--accent: #3498db;  /* Change l'orange en bleu */
```

### Modifier la police

Trouvez dans `style.css` :

```css
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&display=swap');
```

Changez `Outfit` par une autre police Google Fonts.

---

## 📤 Comment Publier les Modifications en Ligne

### Méthode 1 : Via Git (Recommandé)

```bash
# 1. Aller dans le dossier du projet
cd /Users/fayerart/Documents/perso/JM

# 2. Voir les fichiers modifiés
git status

# 3. Ajouter tous les changements
git add -A

# 4. Créer un commit avec un message
git commit -m "Description de vos modifications"

# 5. Envoyer sur GitHub
git push origin main
```

**Render va automatiquement redéployer le site** (2-3 minutes)

### Méthode 2 : Forcer un redéploiement sur Render

Si Render ne détecte pas les changements :

1. Allez sur [dashboard.render.com](https://dashboard.render.com)
2. Cliquez sur votre service **gosmart**
3. Cliquez **"Manual Deploy"** → **"Deploy latest commit"**

---

## 📋 Checklist pour Ajouter une Nouvelle Image

- [ ] Image copiée dans `frontend/static/media/`
- [ ] Nom de fichier sans espaces (utilisez des tirets : `photo-1.jpeg`)
- [ ] Taille raisonnable (< 2 MB)
- [ ] Image ajoutée dans le HTML avec le bon chemin
- [ ] Testée localement avant de publier
- [ ] Modifications commitées et pushées sur GitHub

---

## 🔍 Comment Tester Localement

Avant de publier, testez sur votre ordinateur :

```bash
# 1. Activer l'environnement virtuel
cd /Users/fayerart/Documents/perso/JM
source venv/bin/activate

# 2. Démarrer le serveur
python -m uvicorn backend.main:app --reload

# 3. Ouvrir dans le navigateur
# http://localhost:8000
```

---

## 🗂️ Organisation Recommandée des Médias

```
frontend/static/media/
├── autostable/          # Photos du modèle autostable
│   ├── IMG_0566.jpeg
│   ├── IMG_0567.jpeg
│   └── IMG_0568.jpeg
├── coque/               # Photos du modèle coque
├── handle/              # Photos du modèle poignée
├── mini/                # Photos du modèle mini
├── mural/               # Photos du modèle mural
├── prototypes/          # Photos des prototypes
│   ├── Autostable 15°.jpeg
│   ├── Autostable 45°.jpeg
│   └── ...
├── brevet/             # Documents PDF
│   └── 10864793_Courrier_de_notification (10).pdf
├── IMG_0565.jpeg       # Image hero principale
└── IMG_0940.MOV        # Vidéo de démonstration
```

---

## ⚠️ Erreurs Courantes et Solutions

### L'image ne s'affiche pas

**Vérifiez :**
1. Le chemin est correct : `/static/media/dossier/fichier.jpeg`
2. Le fichier existe bien dans le bon dossier
3. Pas d'espaces dans le nom du fichier (utilisez des tirets)
4. Le fichier a été commité et pushé sur GitHub

### Les modifications ne s'affichent pas sur le site

**Solutions :**
1. Videz le cache du navigateur : `Cmd+Shift+R` (Mac) ou `Ctrl+Shift+R` (Windows)
2. Vérifiez que vous avez bien fait `git push`
3. Attendez 2-3 minutes pour que Render redéploie
4. Forcez un redéploiement manuel sur Render

### La vidéo est trop lourde

**Solutions :**
1. Compressez la vidéo avec un outil comme HandBrake
2. Ou utilisez Git LFS pour les gros fichiers
3. Ou hébergez la vidéo sur YouTube/Vimeo et intégrez-la

---

## 📞 Besoin d'Aide ?

- **Problème technique ?** Vérifiez les logs sur Render
- **Modification complexe ?** Consultez la documentation FastAPI
- **Design à changer ?** Modifiez `style.css`

---

## 🎯 Résumé Rapide

| Action | Fichier à modifier | Commande |
|--------|-------------------|----------|
| Ajouter une photo | `frontend/templates/*.html` | Copier dans `frontend/static/media/` |
| Modifier un texte | `frontend/templates/*.html` | Éditer directement |
| Changer les couleurs | `frontend/static/css/style.css` | Modifier `:root` |
| Ajouter une page | `frontend/templates/nouvelle.html` + `backend/main.py` | Créer fichier + route |
| Publier en ligne | - | `git add -A && git commit -m "..." && git push` |

---

**Bon courage avec la gestion de votre site ! 🚀**
