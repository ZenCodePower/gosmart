# 💡 Exemples Concrets de Modifications

## Exemple 1 : Ajouter une Nouvelle Photo dans la Galerie

### Situation
Vous voulez ajouter une nouvelle photo du modèle Autostable dans la page produits.

### Étapes

**1. Copier la photo :**
```bash
cp "chemin/vers/nouvelle-photo.jpeg" frontend/static/media/autostable/IMG_0569.jpeg
```

**2. Ouvrir `frontend/templates/products.html`**

**3. Trouver la section Autostable (vers la ligne 100) :**
```html
<div class="gallery-grid">
    <div class="gallery-item" onclick="openLightbox('/static/media/autostable/IMG_0566.jpeg')">
        <img src="/static/media/autostable/IMG_0566.jpeg" alt="GOSMART Autostable" loading="lazy">
        ...
    </div>
    <!-- ... autres images ... -->
</div>
```

**4. Ajouter votre nouvelle image :**
```html
<div class="gallery-grid">
    <!-- Images existantes -->
    <div class="gallery-item" onclick="openLightbox('/static/media/autostable/IMG_0566.jpeg')">
        <img src="/static/media/autostable/IMG_0566.jpeg" alt="GOSMART Autostable" loading="lazy">
        <div class="gallery-item-overlay">
            <span class="gallery-item-title" data-fr="Vue 1" data-en="View 1">Vue 1</span>
        </div>
    </div>
    
    <!-- NOUVELLE IMAGE -->
    <div class="gallery-item" onclick="openLightbox('/static/media/autostable/IMG_0569.jpeg')">
        <img src="/static/media/autostable/IMG_0569.jpeg" alt="GOSMART Autostable" loading="lazy">
        <div class="gallery-item-overlay">
            <span class="gallery-item-title" data-fr="Vue 4" data-en="View 4">Vue 4</span>
        </div>
    </div>
</div>
```

**5. Publier :**
```bash
git add frontend/static/media/autostable/IMG_0569.jpeg frontend/templates/products.html
git commit -m "Ajout nouvelle photo Autostable"
git push origin main
```

---

## Exemple 2 : Changer le Texte d'un Titre

### Situation
Vous voulez changer "Modèle Autostable" en "Modèle Autostable Premium"

### Étapes

**1. Ouvrir `frontend/templates/products.html`**

**2. Chercher "Modèle Autostable" (Ctrl+F ou Cmd+F)**

**3. Trouver la ligne :**
```html
<h2 data-fr="Modèle Autostable" data-en="Autostable Model">Modèle Autostable</h2>
```

**4. Modifier :**
```html
<h2 data-fr="Modèle Autostable Premium" data-en="Premium Autostable Model">Modèle Autostable Premium</h2>
```

**5. Publier :**
```bash
git add frontend/templates/products.html
git commit -m "Renommage modèle Autostable en Premium"
git push origin main
```

---

## Exemple 3 : Remplacer la Vidéo de Démo

### Situation
Vous avez une nouvelle vidéo de démonstration.

### Étapes

**1. Copier la nouvelle vidéo :**
```bash
cp "chemin/vers/nouvelle-demo.mp4" frontend/static/media/demo-2026.mp4
```

**2. Ouvrir `frontend/templates/index.html`**

**3. Trouver la section vidéo (vers la ligne 89) :**
```html
<video id="demo-video" controls poster="/static/media/IMG_0565.jpeg">
    <source src="/static/media/IMG_0940.MOV" type="video/quicktime">
</video>
```

**4. Remplacer :**
```html
<video id="demo-video" controls poster="/static/media/IMG_0565.jpeg">
    <source src="/static/media/demo-2026.mp4" type="video/mp4">
</video>
```

**5. Publier :**
```bash
git add frontend/static/media/demo-2026.mp4 frontend/templates/index.html
git commit -m "Nouvelle vidéo de démonstration"
git push origin main
```

---

## Exemple 4 : Ajouter un Nouveau Modèle

### Situation
Vous voulez ajouter un nouveau modèle "Pro" avec ses photos.

### Étapes

**1. Créer le dossier et copier les photos :**
```bash
mkdir -p frontend/static/media/pro
cp "chemin/vers/photo1.jpeg" frontend/static/media/pro/
cp "chemin/vers/photo2.jpeg" frontend/static/media/pro/
```

**2. Ouvrir `frontend/templates/products.html`**

**3. Ajouter une nouvelle section après le modèle Mini :**
```html
<!-- Modèle Pro Section -->
<section style="background: var(--secondary);">
    <div class="container">
        <div class="section-header">
            <span class="section-tag" data-fr="Modèle Pro" data-en="Pro Model">Modèle Pro</span>
            <h2 data-fr="Modèle Pro" data-en="Pro Model">Modèle Pro</h2>
            <p data-fr="Description du modèle Pro..." data-en="Pro model description...">Description du modèle Pro...</p>
        </div>
        <div class="gallery-grid">
            <div class="gallery-item" onclick="openLightbox('/static/media/pro/photo1.jpeg')">
                <img src="/static/media/pro/photo1.jpeg" alt="GOSMART Pro" loading="lazy">
                <div class="gallery-item-overlay">
                    <span class="gallery-item-title" data-fr="Vue 1" data-en="View 1">Vue 1</span>
                </div>
            </div>
            <div class="gallery-item" onclick="openLightbox('/static/media/pro/photo2.jpeg')">
                <img src="/static/media/pro/photo2.jpeg" alt="GOSMART Pro" loading="lazy">
                <div class="gallery-item-overlay">
                    <span class="gallery-item-title" data-fr="Vue 2" data-en="View 2">Vue 2</span>
                </div>
            </div>
        </div>
    </div>
</section>
```

**4. Publier :**
```bash
git add -A
git commit -m "Ajout nouveau modèle Pro"
git push origin main
```

---

## Exemple 5 : Modifier les Couleurs du Site

### Situation
Vous voulez changer la couleur orange en bleu.

### Étapes

**1. Ouvrir `frontend/static/css/style.css`**

**2. Trouver la section `:root` (ligne ~10) :**
```css
:root {
    --accent: #ff6b35;        /* Orange actuel */
    --accent-light: #ff8c5a;
    --accent-dark: #e55a2b;
}
```

**3. Remplacer par du bleu :**
```css
:root {
    --accent: #3498db;        /* Bleu */
    --accent-light: #5dade2;
    --accent-dark: #2874a6;
}
```

**4. Publier :**
```bash
git add frontend/static/css/style.css
git commit -m "Changement couleur orange vers bleu"
git push origin main
```

---

## Exemple 6 : Ajouter une Section dans la Page d'Accueil

### Situation
Vous voulez ajouter une section "Témoignages" sur la page d'accueil.

### Étapes

**1. Ouvrir `frontend/templates/index.html`**

**2. Trouver un endroit approprié (par exemple après la section Features)**

**3. Ajouter la nouvelle section :**
```html
<!-- Témoignages Section -->
<section style="background: var(--secondary);">
    <div class="container">
        <div class="section-header">
            <span class="section-tag" data-fr="Témoignages" data-en="Testimonials">Témoignages</span>
            <h2 data-fr="Ce que disent nos utilisateurs" data-en="What our users say">Ce que disent nos utilisateurs</h2>
        </div>
        <div class="features-grid">
            <div class="feature-card">
                <p data-fr="« Excellent produit, très pratique ! »" data-en="« Excellent product, very practical! »">« Excellent produit, très pratique ! »</p>
                <p style="margin-top: 15px; color: var(--accent);">- Jean D.</p>
            </div>
            <div class="feature-card">
                <p data-fr="« Design moderne et fonctionnel. »" data-en="« Modern and functional design. »">« Design moderne et fonctionnel. »</p>
                <p style="margin-top: 15px; color: var(--accent);">- Marie L.</p>
            </div>
        </div>
    </div>
</section>
```

**4. Publier :**
```bash
git add frontend/templates/index.html
git commit -m "Ajout section témoignages"
git push origin main
```

---

## 📝 Notes Importantes

- **Toujours tester localement** avant de publier
- **Utiliser des noms de fichiers clairs** sans espaces
- **Respecter la structure** existante pour la cohérence
- **Commit avec des messages clairs** pour faciliter le suivi
- **Vérifier le rendu** après chaque modification

---

**Ces exemples couvrent 90% des cas d'usage courants !**
