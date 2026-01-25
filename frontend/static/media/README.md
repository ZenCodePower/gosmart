# Dossier Media

Placez vos photos et vidéos de démonstration du GOSMART dans ce dossier.

## Format recommandé

- **Photos** : JPG, PNG (résolution recommandée : 1920x1080 ou supérieure)
- **Vidéos** : MP4 (format recommandé pour la compatibilité web)

## Exemples d'utilisation

### Pour ajouter une photo dans la galerie :

Modifiez `frontend/templates/index.html` et remplacez un placeholder par :

```html
<div class="gallery-item">
    <img src="/static/media/votre-photo.jpg" alt="GOSMART en situation" style="width: 100%; height: 100%; object-fit: cover;">
</div>
```

### Pour ajouter une vidéo :

```html
<div class="gallery-item">
    <video controls style="width: 100%; height: 100%; object-fit: cover;">
        <source src="/static/media/demo.mp4" type="video/mp4">
        Votre navigateur ne supporte pas la lecture de vidéos.
    </video>
</div>
```

