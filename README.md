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

Modul pertama yang mencakup semua konsep dasar (CRUD, Views, Security, API).
Detail selengkapnya baca di [README Modul Todo List](./todo_list/README.md).

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
