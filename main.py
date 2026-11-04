
from fastapi import FastAPI

app = FastAPI(
    title="PRu API",
    description="Personal API developed by PRu",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "nama": "PRu API",
        "status": "aktif",
        "versi": "1.0.0",
        "pesan": "Selamat datang di PRu API!"
    }

@app.get("/status")
def status():
    return {
        "status": "online",
        "developer": "PRu"
}
  
