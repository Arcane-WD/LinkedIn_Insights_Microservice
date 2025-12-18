# LinkedIn Insights Microservice

A backend microservice that fetches, stores, and serves insights for LinkedIn company pages using authenticated scraping.
The service supports lazy scraping, persistent storage, Redis-based caching, advanced search filters, pagination, and robust error handling.

---

## 📌 Problem Overview

Given a LinkedIn **Page ID** (last part of the LinkedIn URL), the service:

- Scrapes company insights from LinkedIn (authenticated)
- Stores the data in a relational database
- Serves the data via RESTful APIs
- Avoids repeated scraping using database persistence and Redis caching

Example:

```

[https://www.linkedin.com/company/deepsolv/](https://www.linkedin.com/company/deepsolv/)
Page ID → deepsolv

````

---

## ✅ Features Implemented

### Core Functionality

- Scrapes LinkedIn company pages using Page ID
- Stores company data in SQLite using SQLAlchemy
- Lazy scraping (scrape only if data not present)
- Handles invalid / non-company pages gracefully
- Advanced search with filters:
  - Industry
  - Employee count range
- Pagination support
- RESTful API design using FastAPI
- Modular, maintainable backend structure
- Postman collection for API testing

### Caching & Performance

- Redis-based caching for:
  - Company lookups
  - Search queries
- TTL-based cache invalidation
- SQLite remains the source of truth

---

## 🛠️ Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Database:** SQLite
- **Cache:** Redis
- **Scraping:** Selenium + linkedin-scraper
- **Auth:** Cookie-based LinkedIn login
- **API Testing:** Postman
- **Containerization:** Docker (optional)

---

## 🔄 Update Timeline

- **Dec 13–14, 2025:** Core API, DB persistence, scraping, error handling
- **Dec 16, 2025:** Redis integration for company caching
- **Dec 17, 2025:** Search endpoint caching + Docker Compose setup

---

## 🐳 Docker Usage & Scraping Behavior

Docker support is included to demonstrate system design and infrastructure awareness.

### Important Note on Scraping in Docker

- Selenium-based scraping **requires a full browser environment**
- Minimal Docker images do not include Chrome or display dependencies
- As a result, **scraping is disabled when running inside Docker**

Docker is intended for:
- API execution
- Redis integration
- Cache-backed reads
- Architecture demonstration

Scraping is expected to run:
- Locally (developer machine)
- Or in non-containerized production environments (e.g. Render)

This design choice is intentional and documented.

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
LINKEDIN_EMAIL=your_linkedin_email
LINKEDIN_PASSWORD=your_linkedin_password
REDIS_HOST=localhost
REDIS_PORT=6379
````

### Notes

* LinkedIn credentials are required **only by the backend scraper**
* End users never provide LinkedIn credentials
* `.env`, cookies, and database files are ignored via `.gitignore`

---

## ▶️ Running the Application (Local)

```bash
python -m uvicorn app.main:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

---

## ▶️ Running with Docker (No Scraping)

```bash
docker compose up --build
```

* API available at `http://localhost:8000`
* Redis runs automatically
* Cached and DB-backed reads work
* Scraping is intentionally disabled

---

## 🔁 Data Flow (Lazy Scraping)

1. Client requests `/companies/{page_id}`
2. Service checks Redis cache
3. Falls back to database
4. If not found:

   * Scrapes LinkedIn (only when scraping is enabled)
   * Stores data
   * Caches response
5. Invalid pages are persisted to avoid repeated scraping

---

## ⚠️ Limitations & Notes

* Scraping depends on LinkedIn UI stability and rate limits
* Selenium is blocking (async scraping not implemented)
* SQLite is used for simplicity
* Docker mode disables scraping by design
* Intended for educational and evaluation purposes only

---

````


