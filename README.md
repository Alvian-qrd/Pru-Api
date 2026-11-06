# Pru-Api

Personal API built with FastAPI, SQLAlchemy, and PostgreSQL (SQLite is used locally by default).

## Menjalankan secara lokal

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

API berjalan di `http://127.0.0.1:8000`; dokumentasi interaktif ada di `http://127.0.0.1:8000/docs`. Database SQLite lokal dibuat otomatis sebagai `pru_api.db`.

Untuk lingkungan produksi, atur `DATABASE_URL` ke URL PostgreSQL dan `SECRET_KEY` ke nilai rahasia yang kuat. Contoh membuat secret:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## Autentikasi

Buat akun dengan `POST /auth/register`:

```json
{"username":"alvian","password":"password-yang-kuat"}
```

Login melalui `POST /auth/login` menggunakan form URL-encoded dengan field `username` dan `password`. Respons berisi access token Bearer yang berlaku selama 60 menit. Masukkan token melalui tombol **Authorize** di `/docs`, atau kirim header `Authorization: Bearer <token>`.

`GET /auth/me` menampilkan akun yang sedang terautentikasi.

## CRUD item

Semua endpoint item memerlukan token. Data item hanya dapat dibaca atau diubah oleh pemiliknya.

- `POST /items` — buat item (`title`, opsional `description`).
- `GET /items` — daftar item milik akun.
- `GET /items/{item_id}` — baca satu item.
- `PUT /items/{item_id}` — ubah item.
- `DELETE /items/{item_id}` — hapus item.

## Deploy ke Render

File `render.yaml` menyiapkan web service dan PostgreSQL. Di Render, pilih **New + → Blueprint**, hubungkan repositori ini, lalu ikuti petunjuknya. Render akan membuat `DATABASE_URL` dan `SECRET_KEY` dari konfigurasi; jangan commit secret ke repositori.
