# 🚀 Guide de Déploiement GOSMART

## Option recommandée : Render (GRATUIT) + Domaine (~9€/an)

---

## Étape 1 : Acheter le domaine (5 min)

### Vérifier la disponibilité

1. Allez sur **[porkbun.com](https://porkbun.com)** (le moins cher)
2. Recherchez votre domaine souhaité :
   - `gosmart.com` (~9$/an) - probablement pris
   - `gosmart.fr` (~7€/an) - bonne alternative française
   - `gosmart-support.com`
   - `go-smart.fr`

### Alternatives de registraires (si Porkbun ne convient pas)

| Registraire | Prix .com/an | Prix .fr/an | WHOIS Privacy |
|-------------|-------------|-------------|---------------|
| **Porkbun** | ~9$ | - | ✅ Gratuit |
| **Namecheap** | ~10$ | - | ✅ Gratuit |
| **OVH** | ~10€ | ~7€ | ✅ Gratuit |
| **Gandi** | ~15€ | ~12€ | ✅ Inclus |
| **Ionos** | ~1€ 1ère année | ~1€ | ⚠️ Payant |

### Lors de l'achat, activez :
- ✅ WHOIS Privacy (gratuit sur Porkbun/Namecheap)
- ✅ Auto-renewal (renouvellement automatique)
- ✅ 2FA sur votre compte

---

## Étape 2 : Créer un compte GitHub (2 min)

1. Allez sur **[github.com](https://github.com)**
2. Créez un compte gratuit
3. Créez un nouveau repository nommé `gosmart`

---

## Étape 3 : Uploader le code sur GitHub (5 min)

Dans le terminal, depuis le dossier JM :

```bash
cd /Users/fayerart/Documents/perso/JM

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Premier commit
git commit -m "Initial commit - GOSMART website"

# Lier à votre repository GitHub (remplacez VOTRE_USERNAME)
git remote add origin https://github.com/VOTRE_USERNAME/gosmart.git

# Pousser le code
git branch -M main
git push -u origin main
```

---

## Étape 4 : Déployer sur Render (5 min)

1. Allez sur **[render.com](https://render.com)**
2. Créez un compte (gratuit) avec GitHub
3. Cliquez sur **"New +"** → **"Web Service"**
4. Connectez votre repository GitHub `gosmart`
5. Configuration :
   - **Name** : `gosmart`
   - **Runtime** : `Python 3`
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Plan** : `Free`
6. Cliquez **"Create Web Service"**

⏳ Attendez 2-3 minutes, votre site sera accessible sur :
`https://gosmart.onrender.com`

---

## Étape 5 : Connecter votre domaine (5 min)

### Sur Render :
1. Allez dans votre service → **Settings** → **Custom Domains**
2. Cliquez **"Add Custom Domain"**
3. Entrez votre domaine : `gosmart.com` (ou `gosmart.fr`)
4. Render vous donnera des enregistrements DNS à configurer

### Sur votre registraire (Porkbun/OVH/etc.) :
1. Allez dans la gestion DNS de votre domaine
2. Ajoutez les enregistrements fournis par Render :

**Option A - CNAME (recommandé pour sous-domaine www):**
```
Type: CNAME
Name: www
Value: gosmart.onrender.com
```

**Option B - Pour le domaine racine :**
```
Type: A
Name: @
Value: [IP fournie par Render]
```

3. Attendez 10-30 minutes pour la propagation DNS

---

## Étape 6 : SSL/HTTPS (automatique)

Render configure automatiquement le certificat SSL (HTTPS) pour votre domaine. Votre site sera sécurisé !

---

## 📊 Récapitulatif des coûts

| Service | Coût |
|---------|------|
| Domaine .com (Porkbun) | ~9$/an |
| Hébergement Render | **GRATUIT** |
| SSL/HTTPS | **GRATUIT** |
| **TOTAL** | **~9$/an** |

---

## ⚠️ Limitations du plan gratuit Render

- Le site "s'endort" après 15 min d'inactivité (redémarre en ~30s au premier accès)
- 750 heures de fonctionnement/mois
- Parfait pour un site vitrine/portfolio

### Pour éviter l'endormissement (optionnel) :
Utilisez un service de ping gratuit comme **UptimeRobot** pour garder le site actif.

---

## 🆘 En cas de problème

1. Vérifiez les logs sur Render (Dashboard → Logs)
2. Assurez-vous que tous les fichiers sont sur GitHub
3. Vérifiez que le `requirements.txt` est à la racine

---

## 📁 Fichiers de configuration créés

- `Procfile` - Configuration pour l'hébergement
- `render.yaml` - Configuration Render
- `runtime.txt` - Version Python

Votre site est prêt à être déployé ! 🎉
