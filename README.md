# PS-CRM — Public Services CRM

A full-stack municipal management web app built with **Python Flask + SQLite**.
3 user roles · 24 pages · Complaint tracking · Image uploads · Budget management

---

## Quick Start (3 Steps)

### Step 1 — Install Python (if not already)
Download from https://python.org (version 3.8 or higher)

### Step 2 — Install Flask
Open a terminal / command prompt in the `ps-crm` folder and run:
```
pip install flask werkzeug
```

### Step 3 — Run the app
```
python run.py
```

That's it! The database is created automatically on first run.

---

## Demo Login Credentials

| Role | Email | Password |
|---|---|---|
| 🔴 Admin | admin@pscrm.in | admin123 |
| 🟡 Municipal Head | head@pscrm.in | head123 |
| 🟢 Citizen | citizen@pscrm.in | citizen123 |
| 🟢 Citizen 2 | priya@pscrm.in | priya123 |

---

## Project Structure

```
ps-crm/
│
├── run.py               ← START HERE — run this to launch the app
├── app.py               ← Flask app, auth routes, session management
├── database.py          ← SQLite schema + seed data
├── requirements.txt     ← Python dependencies
│
├── routes/
│   ├── admin.py         ← All admin routes (10 pages)
│   ├── citizen.py       ← All citizen routes (7 pages)
│   └── head.py          ← All municipal head routes (7 pages)
│
├── templates/
│   ├── auth/
│   │   ├── login.html        ← Login page (role selector + demo creds)
│   │   └── register.html     ← Citizen self-registration
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── complaints.html
│   │   ├── complaint_detail.html
│   │   ├── notices.html
│   │   ├── labour.html
│   │   ├── budget.html
│   │   ├── problemgram.html
│   │   ├── departments.html
│   │   ├── calendar.html
│   │   └── users.html
│   ├── citizen/
│   │   ├── dashboard.html
│   │   ├── complaints.html
│   │   ├── complaint_detail.html
│   │   ├── new_complaint.html
│   │   ├── notices.html
│   │   ├── problemgram.html
│   │   └── city_issues.html
│   ├── head/
│   │   ├── dashboard.html
│   │   ├── overview.html
│   │   ├── budget.html
│   │   ├── labour.html
│   │   ├── notices.html
│   │   ├── departments.html
│   │   └── calendar.html
│   └── shared/
│       ├── base.html     ← Master layout (sidebar, topbar, flash messages)
│       ├── profile.html
│       └── 404.html
│
└── static/
    └── uploads/          ← Complaint images saved here (auto-created)
```

---

## Features by Role

### 🔴 Admin
| Feature | Details |
|---|---|
| Dashboard | Stats, recent complaints, dept overview, budget bars, notices, calendar |
| Complaints | Filter by status/priority/dept · Update status · Add timeline notes |
| Complaint Detail | Full info · Image view · Activity timeline · Status update |
| Notices | Post notices (Budget/Rules/Tender/Emergency/Forum) · Delete |
| Labour | Add/remove workers · Update attendance status · Filter by dept |
| Budget | Per-dept allocation vs spending · Add entries · Progress bars |
| Problemgram | Post updates (citizens read-only) · Pin/unpin · Delete |
| Departments | 6-card overview with links to complaints and labour |
| Calendar | Add/delete events with type, dept, date |
| Users | View all users · Enable/disable accounts |

### 🟡 Municipal Head
| Feature | Details |
|---|---|
| Dashboard | City-wide stats · Dept health bars · Priority breakdown · Critical issues |
| All Complaints | Read-only city-wide complaints table with filters |
| Budget | Per-dept cards with allocated/spent/remaining + progress bars |
| Labour | Per-dept active/absent/on-leave/vacant breakdown + full table |
| Notices | Read all · Post new notices as Municipal Head |
| Departments | Full performance report table |
| Calendar | Read-only view of all events |

### 🟢 Citizen
| Feature | Details |
|---|---|
| Dashboard | My stats · My recent complaints · Notices · Problemgram feed · Events |
| My Complaints | List with status filter · Track each complaint |
| File Complaint | Title · Dept · Priority · Area · Description · **Image Upload** |
| Complaint Detail | Full info · **Live tracking timeline** with colour-coded steps |
| Notices | All public notices with type filter tabs |
| Problemgram | Read-only feed of admin posts · Filter by department |
| City Issues | Anonymous feed of all city complaints |

---

## Database Tables

| Table | Purpose |
|---|---|
| `users` | Admin, Head, Citizens with roles |
| `departments` | 6 departments (Road, Water, Electricity, Waste, Sewers, Construction) |
| `complaints` | All filed complaints with status, priority, image path |
| `complaint_updates` | Timeline entries per complaint |
| `notices` | Public announcements |
| `budget_entries` | Allocated/Spent/Returned per department |
| `posts` | Problemgram posts (admin-only) |
| `labour` | Workers with attendance status |
| `events` | Calendar events |

---

## URL Reference

### Auth
| URL | Description |
|---|---|
| `/` | Redirects to login or dashboard |
| `/login` | Login page |
| `/register` | Citizen self-registration |
| `/logout` | Clear session |
| `/profile` | Edit profile |

### Admin `/admin/...`
| URL | Description |
|---|---|
| `/admin/dashboard` | Main dashboard |
| `/admin/complaints` | All complaints |
| `/admin/complaints/<id>` | Complaint detail + update |
| `/admin/notices` | Notices management |
| `/admin/labour` | Labour management |
| `/admin/budget` | Budget management |
| `/admin/problemgram` | Post management |
| `/admin/departments` | Dept overview |
| `/admin/calendar` | Events |
| `/admin/users` | User management |

### Citizen `/citizen/...`
| URL | Description |
|---|---|
| `/citizen/dashboard` | Home |
| `/citizen/complaints` | My complaints |
| `/citizen/complaints/new` | File complaint |
| `/citizen/complaints/<id>` | Track complaint |
| `/citizen/notices` | Read notices |
| `/citizen/problemgram` | Read posts |
| `/citizen/city-issues` | City-wide feed |

### Municipal Head `/head/...`
| URL | Description |
|---|---|
| `/head/dashboard` | City overview |
| `/head/overview` | All complaints |
| `/head/budget` | Budget report |
| `/head/labour` | Labour report |
| `/head/notices` | Notices + post |
| `/head/departments` | Dept report |
| `/head/calendar` | Events |

---

## Troubleshooting

**Port already in use?**
```
python run.py
# If port 5000 is busy, edit run.py and change port=5000 to port=5001
```

**Database reset (fresh start)?**
```
# Delete pscrm.db and run again — it auto-recreates with seed data
del pscrm.db        (Windows)
rm pscrm.db         (Mac/Linux)
python run.py
```

**Image uploads not working?**
Make sure the `static/uploads/` folder exists. It's auto-created by `run.py`.

**Module not found?**
```
pip install flask werkzeug
```

---

## Tech Stack

- **Backend:** Python 3 + Flask 3
- **Database:** SQLite (built into Python — no install needed)
- **Auth:** Session-based with Werkzeug password hashing
- **Frontend:** Pure HTML + CSS (no frameworks — zero npm install)
- **Fonts:** Google Fonts (Syne + DM Sans)
- **File Uploads:** Werkzeug secure_filename

---

Built for PS-CRM · Municipal Management Platform · 2026
