# Odoo ERP Training

Belajar membangun modul Odoo dari nol — mulai dari struktur dasar sampai multi-user dengan REST API.

---

## Modul yang Dibangun

| # | Modul | Topik yang Dipelajari |
|---|---|---|
| 01 | [`todo_list/`](./todo_list/) | Struktur dasar modul Odoo |

---

## Roadmap Belajar

### ✅ 01 — `todo_list` · Todo List App

Modul pertama. Mencakup semua konsep dasar yang dibutuhkan sebelum masuk ke modul yang lebih kompleks.

**Yang dipelajari:**

- Struktur folder modul Odoo (`__manifest__`, `models`, `views`, `controllers`, `security`)
- Membuat Model dan field (`Char`, `Boolean`, `Text`, `Many2one`)
- Membuat tampilan backend otomatis: List, Form, Kanban, Search
- Membuat halaman web publik dengan QWeb template
- Membuat REST API sederhana (GET, POST, PUT, DELETE)
- Sistem keamanan: Grup (Role), Record Rules, dan Access Rights (CSV)
- Multi-user: User hanya lihat data miliknya, Manager lihat semua

**File utama:**

```
todo_list/
├── __manifest__.py          # Deklarasi modul
├── models/models.py         # Model + field database
├── controllers/controllers.py  # Route + REST API
├── views/views.xml          # UI backend (List/Form/Kanban/Search)
├── views/templates.xml      # Halaman web publik (QWeb)
└── security/
    ├── security.xml         # Grup & Record Rules
    └── ir.model.access.csv  # Izin CRUD per model
```

**Akun testing:**

| Login | Password | Role |
|---|---|---|
| `admin` | `admin` | Manager — lihat semua task |
| `user` | `user` | User biasa — lihat task sendiri |

**URL:**

- Backend → `http://localhost:8070`
- Frontend → `http://localhost:8070/tugas`
- API → `http://localhost:8070/api/tasks`

---

### 🔲 02 — Inheritance · Extend Modul yang Sudah Ada

> Belum dibuat.

Yang akan dipelajari: `_inherit`, menambah field ke model bawaan Odoo (misal `res.partner`), extend view dengan `xpath`.

---

### 🔲 03 — Relasi Antar Model

> Belum dibuat.

Yang akan dipelajari: `Many2one`, `One2many`, `Many2many`, computed field (`@api.depends`), onchange (`@api.onchange`).

---

### 🔲 04 — Wizard & Laporan

> Belum dibuat.

Yang akan dipelajari: `TransientModel` untuk wizard/popup, cetak laporan PDF dengan QWeb Report.

---

### 🔲 05 — Scheduled Action & Automation

> Belum dibuat.

Yang akan dipelajari: Cron job terjadwal, Server Action, Automation Rules.

---

## Menjalankan Server

```powershell
# Jalankan server
& "D:\Koding\Odoo\odoo-19\python\python.exe" `
  "D:\Koding\Odoo\odoo-19\server\odoo-bin" `
  -c todo_list/odoo.conf -d odoo --http-port 8070

# Update modul setelah ada perubahan kode
& "D:\Koding\Odoo\odoo-19\python\python.exe" `
  "D:\Koding\Odoo\odoo-19\server\odoo-bin" `
  -c todo_list/odoo.conf -d odoo -u todo_list --http-port 8070
```
