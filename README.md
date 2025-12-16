---

# LinkedIn Insights Microservice

A backend microservice that fetches, stores, and serves insights for LinkedIn company pages using authenticated scraping.
The service supports lazy scraping, persistent storage, advanced search filters, pagination, and robust error handling.

---

## 📌 Problem Overview

Given a LinkedIn **Page ID** (last part of the LinkedIn URL), the service:

* Scrapes company insights from LinkedIn
* Stores the data in a relational database
* Serves the data via RESTful APIs
* Avoids re-scraping using database persistence and caching

Example:

```
https://www.linkedin.com/company/deepsolv/
Page ID → deepsolv
```

---

## ✅ Features Implemented

### Mandatory Requirements

* Scrapes LinkedIn company pages using Page ID
* Stores company data in SQLite using SQLAlchemy
* Lazy scraping (scrape only if data not present in DB)
* Handles invalid / non-company pages gracefully
* Advanced search with filters:

  * Industry
  * Employee count range
* Pagination support
* RESTful API design using FastAPI
* Well-structured, modular backend code
* Postman collection for API testing

### Bonus (Partial)

* Cookie-based authentication to avoid repeated logins
* Lightweight in-memory caching with TTL to reduce scraping

---

## 🔄 Update: Redis Caching (Added)

A **rudimentary Redis-based caching layer** has been added to reduce repeated database access and avoid unnecessary scraping for frequently requested company pages.

Redis is used strictly as an **in-memory cache**.
SQLite remains the source of truth.

---

## ▶️ Running Redis Alongside the Application

Redis is **optional but recommended** for improved performance.

### Option 1: Run Redis using Docker (Recommended)

1. Install Docker Desktop
   [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

2. Ensure Docker is running:

```bash
docker --version
```

3. Start Redis:

```bash
docker run -d -p 6379:6379 redis:7
```

4. Verify Redis is running:

```bash
docker ps
```

---

### Option 2: Run Redis without Docker

If Redis is installed locally, ensure it is running on:

```
Host: localhost
Port: 6379
```

---

## ⚙️ Redis Configuration

The application connects to Redis using the following environment variables (optional):

```env
REDIS_HOST=localhost
REDIS_PORT=6379
```

If not provided, default values are used.

---

## ▶️ Running the Application (with Redis)

```bash
python -m run uvicorn app.main:app --reload
```

Redis will be automatically used for caching company lookups when available.

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Framework:** FastAPI
* **ORM:** SQLAlchemy
* **Database:** SQLite
* **Scraping:** Selenium + linkedin-scraper
* **Auth:** Cookie-based LinkedIn login
* **API Testing:** Postman
* **Cache:** Redis

---

## 📂 Project Structure

```
deepsolv_project/
├─ app/
│  ├─ api/pages.py
│  ├─ services/
│  │  ├─ page_service.py
│  │  └─ scrapper/
│  │     ├─ auth.py
│  │     └─ company_scraper.py
│  ├─ database.py
│  ├─ models.py
│  ├─ config.py
│  └─ main.py
├─ scripts/
├─ linkedin_insights.postman_collection.json
├─ pyproject.toml
├─ .env
└─ README.md
```

---

## 🔐 Environment Variables (Required)

Create a `.env` file in the project root:

```env
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password
```

### Notes

* Credentials are required for authenticated scraping
* Cookies are stored locally to avoid repeated logins
* `.env`, cookies, and database files are ignored via `.gitignore`

---

## ▶️ Setup & Run Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd deepsolv_project
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python -m uvicorn app.main:app --reload
```

### 5. Open API docs

```
http://127.0.0.1:8000/docs
```

---

## 🔁 Data Flow (Lazy Scraping)

1. Client requests `/companies/{page_id}`
2. Service checks database
3. If not found:

   * Scrapes LinkedIn
   * Stores data
   * Returns response
4. Invalid pages are marked to prevent repeated scraping

---

## 🔍 API Endpoints

### Get company by Page ID

```
GET /companies/{page_id}
```

### List all companies

```
GET /companies
```

### Search companies with filters

```
GET /companies/search?industry=Software&min_size=50&max_size=500
```

Supports pagination via `limit` and `offset`.

---

## 🧪 Postman Collection

A Postman collection is provided:

```
linkedin_insights.postman_collection.json
```

Import this file into Postman to test all APIs. 

---

## ⚠️ Limitations & Notes

* Scraping depends on LinkedIn UI stability
* Selenium is blocking (async scraping not implemented)
* SQLite is used for simplicity and local demo purposes
* Intended for educational and assignment evaluation only

---
