"""
Render / production: run the app bound to 0.0.0.0 and PORT from environment.
"""
import os
import uvicorn
from backend.main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
