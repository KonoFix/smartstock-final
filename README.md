# 📦 SmartStock - Intelligent Inventory Management / Gestão de Estoque Inteligente

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

### 📖 About the Project
**SmartStock** is a web application designed to help small businesses and NGOs manage their inventory efficiently. Developed as a **University Extension Project**, it aims to solve the problem of stockouts and disorganized management in local communities.

This project is aligned with the **UN Sustainable Development Goals (SDGs)**:
* **SDG 8:** Decent Work and Economic Growth (by improving productivity).
* **SDG 9:** Industry, Innovation, and Infrastructure (by implementing digital transformation).

### ✨ Key Features
* **Product Registration:** Complete management of items with cost and pricing.
* **Smart Stock Tracking:** Visual indicators of current stock levels.
* **Automated Restock Alerts:** Utilizing **Django Signals**, the system automatically generates a "Restock Request" whenever a product's quantity falls below the minimum threshold. No manual check needed!
* **Cloud Architecture:** Database hosted on Supabase (PostgreSQL) and application containerized with Docker.

### 🛠️ Tech Stack
* **Backend:** Python & Django Framework.
* **Database:** PostgreSQL (via Supabase).
* **DevOps:** Docker & Docker Compose.
* **Server:** Gunicorn (Production ready).
* **Deployment:** Render (PaaS).

### 🚀 How to Run Locally

#### Prerequisites
* Python 3.9+
* Git

#### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/KonoFix/smartstock-final.git
    cd smartstock-final
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your credentials:
    ```env
    DEBUG=True
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=postgresql://user:password@host:port/database
    ```

5.  **Run Migrations & Start Server:**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### 🐳 Running with Docker
If you have Docker installed, simply run:
```bash
docker build . -t smartstock
docker run --env-file .env -p 8000:8000 smartstock
