# 🚀 TaskEngine.ai: Enterprise Task Intelligence

**TaskEngine.ai** is a high-performance Django 6.0 application designed for real-time operational oversight. It moves beyond traditional "To-Do" lists by integrating **Heuristic Analysis** to provide automated system health insights and a high-speed **HTMX-powered** live interface.

---

## ✨ Key Exceptional Features

* **🧠 Automated Insights Engine:** Uses custom heuristic logic to evaluate system health (Stable, Warning, Critical) and provides actionable advice based on task density and priority bottlenecks.
* **⚡ HTMX Live Search:** Instant, zero-reload filtering of the task database using asynchronous partial page updates.
* **📊 Enterprise Dashboard:** A "Glassmorphic" UI with real-time KPI tracking (Efficiency Score, Critical Throughput, and Active Backlog).
* **🎯 Smart Prioritization:** A multi-level priority system (L1-L5) with dynamic UI color-coding based on urgency.
* **📈 Analytical Deep-Dive:** A dedicated "Dark Mode" analytics view featuring **Chart.js** for visual data distribution.

---

## 📸 System Previews

### 1. Main Operational Dashboard
> *Real-time KPI tracking and the Automated Insights bar.*
![Dashboard Screenshot](/dashboard.png)

### 2. Live Search & Filtering
> *HTMX-powered instant search results without page refresh.*
![Search Screenshot](./screenshots/search.png)

### 3. Advanced Analytics View
> *Dark-themed data visualization using Chart.js.*
![Analytics Screenshot](/insight.png)

---

## 🛠️ Tech Stack

* **Backend:** Python 3.12, Django 6.0
* **Frontend:** Tailwind CSS, HTMX, Animate.css
* **Visuals:** Chart.js
* **Deployment:** Render + WhiteNoise (Optimized Static Delivery)
* **Database:** PostgreSQL (Production)

---

## ⚙️ Installation & Database Setup Guide

### 1. Environment Initialization
```bash
# Clone the repository
git clone [https://github.com/yourusername/enterprise-task-engine.git](https://github.com/yourusername/enterprise-task-engine.git)
cd enterprise-task-engine

# Create & Activate Virtual Environment
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install Dependencies
pip install django django-environ whitenoise gunicorn dj-database-url
pip freeze > requirements.txt
2. Database Configuration (settings.py)
The engine is configured to automatically switch between SQLite (Local) and PostgreSQL (Production).

Python
import dj_database_url
import os

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3'),
        conn_max_age=600
    )
}
3. Static Files Configuration
Essential for the "Enterprise" UI to load correctly on servers.

Python
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
4. Database Migrations & Superuser
Bash
# Apply Database Schema
python manage.py makemigrations
python manage.py migrate

python manage.py runserver


   
