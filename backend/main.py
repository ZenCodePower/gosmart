from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the project root directory (parent of backend)
BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="GOSMART - Support Smartphone Multi-Orientable")

# Mount static files (CSS, JS, images, videos)
# /static/* for canonical URLs; /media, /css, /js so requests without /static prefix also work
static_dir = BASE_DIR / "frontend" / "static"
app.mount("/media", StaticFiles(directory=str(static_dir / "media")), name="media")
app.mount("/css", StaticFiles(directory=str(static_dir / "css")), name="css")
app.mount("/js", StaticFiles(directory=str(static_dir / "js")), name="js")
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# Templates directory
templates_dir = BASE_DIR / "frontend" / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

# Contact submissions storage (in production, use a database)
CONTACTS_FILE = BASE_DIR / "contacts.json"

def load_contacts():
    """Load contact submissions from file"""
    if CONTACTS_FILE.exists():
        with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_contact(contact_data: dict):
    """Save contact submission to file"""
    contacts = load_contacts()
    contact_data["timestamp"] = datetime.now().isoformat()
    contacts.append(contact_data)
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

# ================================
# Page Routes
# ================================

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Home page"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("index.html", {"request": request, "lang": lang})

@app.get("/products", response_class=HTMLResponse)
async def products_page(request: Request):
    """Products/Gallery page"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("products.html", {"request": request, "lang": lang})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """About/Inventor page"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("about.html", {"request": request, "lang": lang})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    """Contact page"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("contact.html", {"request": request, "lang": lang})

@app.get("/principles", response_class=HTMLResponse)
async def principles_page(request: Request):
    """Principles / Principes page - schematical views and usage modes"""
    lang = request.cookies.get("lang", "fr")
    return templates.TemplateResponse("principles.html", {"request": request, "lang": lang})

# ================================
# API Routes
# ================================

# Contact form: messages are sent to both addresses and marked URGENT
CONTACT_RECIPIENT_EMAILS = ["janmidi@gmail.com", "arthur.fayer@gmail.com"]

def send_contact_email(name: str, email: str, message: str, subject: str, newsletter: bool):
    """Send contact form by email to both recipients. Uses yagmail for better UTF-8 handling.
    Returns (success: bool, error_message: str)"""
    # Fonction pour nettoyer les valeurs du .env (enlever espaces insécables, etc.)
    def clean_env_value(value):
        if not value:
            return value
        # Remplacer les espaces insécables et autres caractères problématiques
        return str(value).replace('\xa0', ' ').replace('\u00a0', ' ').strip()
    
    smtp_user = clean_env_value(os.getenv("SMTP_USER"))
    smtp_password = clean_env_value(os.getenv("SMTP_PASSWORD"))
    
    if not smtp_user or not smtp_password:
        return False, "Configuration SMTP manquante. Veuillez définir SMTP_USER et SMTP_PASSWORD dans le fichier .env"
    
    try:
        import yagmail
        
        # Nettoyer les caractères problématiques (au cas où)
        def clean_for_email(text):
            if not text:
                return ""
            # Remplacer les espaces insécables et autres caractères problématiques
            text = str(text).replace('\xa0', ' ').replace('\u00a0', ' ')
            return text
        
        # Nettoyer les champs
        subject_clean = clean_for_email(subject)
        name_clean = clean_for_email(name)
        message_clean = clean_for_email(message)
        
        # Initialiser yagmail (gère automatiquement l'encodage UTF-8)
        yag = yagmail.SMTP(smtp_user, smtp_password)
        
        # Préparer le contenu du message
        subject_display = f"[URGENT] GOSMART Contact - {subject_clean}"
        
        body = f"""Message depuis le formulaire GOSMART

De : {name_clean} <{email}>
Sujet : {subject_clean}
Newsletter : {"Oui" if newsletter else "Non"}

Message :
{message_clean}

---
Repondre directement a : {email}
"""
        
        # Envoyer à tous les destinataires
        for to in CONTACT_RECIPIENT_EMAILS:
            yag.send(
                to=to,
                subject=subject_display,
                contents=body,
                headers={"Reply-To": email}
            )
        
        yag.close()
        return True, "Email envoyé avec succès"
        
    except ImportError:
        # Fallback vers la méthode SMTP standard si yagmail n'est pas installé
        return False, "yagmail n'est pas installé. Installez-le avec: pip install yagmail"
    except Exception as e:
        error_msg = f"Erreur lors de l'envoi de l'email : {str(e)}"
        print(f"ERREUR EMAIL: {error_msg}")  # Log pour debug
        import traceback
        print(f"TRACEBACK: {traceback.format_exc()}")  # Traceback complet pour debug
        return False, error_msg

@app.post("/api/contact")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    language: str = Form("fr"),
    subject: str = Form("info"),
    newsletter: str = Form("false")
):
    """Handle contact form. Saves to file and, if SMTP_* env vars are set, sends to both janmidi@gmail.com and arthur.fayer@gmail.com."""
    try:
        subject_display = f"[URGENT] {subject}"
        contact_data = {
            "name": name,
            "email": email,
            "message": message,
            "subject": subject,
            "subject_display": subject_display,
            "to_emails": list(CONTACT_RECIPIENT_EMAILS),
            "urgent": True,
            "newsletter": newsletter == "true",
            "language": language
        }
        save_contact(contact_data)
        email_sent, email_error = send_contact_email(name, email, message, subject, newsletter == "true")
        
        # Log email status
        if not email_sent:
            print(f"ATTENTION: Email non envoyé - {email_error}")
            # Le message est quand même sauvegardé, donc on continue

        if language == "fr":
            success_message = "Merci pour votre message ! Nous vous répondrons dans les plus brefs délais."
        else:
            success_message = "Thank you for your message! We will respond as soon as possible."

        return JSONResponse({
            "success": True,
            "message": success_message
        })
    except Exception as e:
        if language == "fr":
            error_message = "Une erreur est survenue. Veuillez réessayer."
        else:
            error_message = "An error occurred. Please try again."

        return JSONResponse({
            "success": False,
            "message": error_message
        }, status_code=500)

@app.get("/api/contacts")
async def get_contacts():
    """Get all contact submissions (for admin purposes)"""
    contacts = load_contacts()
    return JSONResponse(contacts)

@app.get("/api/stats")
async def get_stats():
    """Get contact statistics"""
    contacts = load_contacts()
    return JSONResponse({
        "total_contacts": len(contacts),
        "newsletter_subscribers": sum(1 for c in contacts if c.get("newsletter")),
        "by_subject": {
            subject: sum(1 for c in contacts if c.get("subject") == subject)
            for subject in ["info", "partnership", "patent", "press", "other"]
        }
    })

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8001))
    uvicorn.run(app, host="0.0.0.0", port=port)
