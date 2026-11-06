# Pru-Api

Personal API built with FastAPI.

## Menjalankan secara lokal

1. Buat dan aktifkan virtual environment (opsional, tetapi disarankan):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # .venv\\Scripts\\activate  # Windows PowerShell
   ```

2. Pasang dependensi:

   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan server:

   ```bash
   uvicorn main:app --reload
   ```

Server berjalan di `http://127.0.0.1:8000`. Dokumentasi interaktif tersedia di `http://127.0.0.1:8000/docs`.

## Endpoint

- `GET /` — informasi API.
- `GET /status` — status layanan.
- `GET /health` — health check, mengembalikan `{"status":"ok"}`.
