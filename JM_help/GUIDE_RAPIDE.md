# ⚡ Guide Rapide - Gestion Site GOSMART

## 🖼️ Ajouter une Photo

1. **Copier la photo** dans `frontend/static/media/nom-dossier/`
2. **Ajouter dans le HTML** :
   ```html
   <img src="/static/media/nom-dossier/photo.jpeg" alt="Description">
   ```
3. **Publier** : `git add -A && git commit -m "Ajout photo" && git push`

---

## 🎬 Ajouter une Vidéo

1. **Copier la vidéo** dans `frontend/static/media/`
2. **Remplacer dans le HTML** :
   ```html
   <source src="/static/media/votre-video.mp4" type="video/mp4">
   ```
3. **Publier** : `git add -A && git commit -m "Nouvelle vidéo" && git push`

---

## ✏️ Modifier un Texte

1. **Ouvrir** `frontend/templates/index.html` (ou autre page)
2. **Trouver le texte** et le modifier
3. **Publier** : `git add -A && git commit -m "Modif texte" && git push`

---

## ➕ Ajouter une Page

1. **Créer** `frontend/templates/nouvelle-page.html`
2. **Ajouter la route** dans `backend/main.py` :
   ```python
   @app.get("/nouvelle-page", response_class=HTMLResponse)
   async def nouvelle_page(request: Request):
       return templates.TemplateResponse("nouvelle-page.html", {"request": request})
   ```
3. **Ajouter le lien** dans la navigation de toutes les pages
4. **Publier** : `git add -A && git commit -m "Nouvelle page" && git push`

---

## 🎨 Changer les Couleurs

1. **Ouvrir** `frontend/static/css/style.css`
2. **Modifier** les valeurs dans `:root` :
   ```css
   --accent: #ff6b35;  /* Changez cette couleur */
   ```
3. **Publier** : `git add -A && git commit -m "Nouvelles couleurs" && git push`

---

## 📤 Publier les Modifications

```bash
cd /Users/fayerart/Documents/perso/JM
git add -A
git commit -m "Description des changements"
git push origin main
```

**Render redéploiera automatiquement en 2-3 minutes !**

---

## 📁 Où Mettre les Fichiers

| Type | Dossier |
|------|---------|
| Photos | `frontend/static/media/nom-dossier/` |
| Vidéos | `frontend/static/media/` |
| PDF | `frontend/static/media/brevet/` |
| Pages HTML | `frontend/templates/` |
| Styles CSS | `frontend/static/css/style.css` |

---

## ⚠️ À Retenir

- ✅ Toujours tester localement avant de publier
- ✅ Utiliser des noms de fichiers sans espaces
- ✅ Compresser les images si > 2 MB
- ✅ Vider le cache navigateur si les changements n'apparaissent pas
- ✅ Vérifier les logs Render en cas d'erreur

---

**Pour plus de détails, voir `GUIDE_GESTION.md`**
