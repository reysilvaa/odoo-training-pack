# Todo List App (Modul Odoo)

Modul pertama ini mencakup semua konsep dasar yang dibutuhkan sebelum masuk ke modul yang lebih kompleks di Odoo.

## Yang Dipelajari

- Struktur folder modul Odoo (`__manifest__`, `models`, `views`, `controllers`, `security`)
- Membuat Model dan field (`Char`, `Boolean`, `Text`, `Many2one`)
- Membuat tampilan backend otomatis: List, Form, Kanban, Search
- Membuat halaman web publik dengan QWeb template
- Membuat REST API sederhana (GET, POST, PUT, DELETE)
- Sistem keamanan: Grup (Role), Record Rules, dan Access Rights (CSV)
- Multi-user: User hanya lihat data miliknya, Manager lihat semua

## Struktur File

```text
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

## Akun Testing

| Login | Password | Role |
|---|---|---|
| `admin` | `admin` | Manager — lihat semua task |
| `user` | `user` | User biasa — lihat task sendiri |

## URL Akses

- Backend → `http://localhost:8070`
- Frontend → `http://localhost:8070/tugas`
- API → `http://localhost:8070/api/tasks`
