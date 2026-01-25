from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from datetime import datetime
from pathlib import Path

# Get the project root directory (parent of backend)
BASE_DIR = Path(__file__).parent.parent

app = FastAPI(title="GOSMART - Support Smartphone Multi-Orientable")

# Mount static files (CSS, JS, images, videos)
static_dir = BASE_DIR / "frontend" / "static"
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

# ================================
# API Routes
# ================================

@app.post("/api/contact")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
    language: str = Form("fr"),
    subject: str = Form("info"),
    newsletter: str = Form("false")
):
    """Handle contact form submission"""
    try:
        contact_data = {
            "name": name,
            "email": email,
            "message": message,
            "subject": subject,
            "newsletter": newsletter == "true",
            "language": language
        }
        save_contact(contact_data)
        
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
