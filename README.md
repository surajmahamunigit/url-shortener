# URL Shortener API

A REST API built with FastAPI that allows users to shorten URLs, track click statistics, and manage their links.

## Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - Database ORM
- **SQLite** - Database
- **JWT** - Authentication
- **Pydantic** - Data validation

## Features

- User registration and login with JWT authentication
- Shorten any valid URL
- Redirect short links to original URLs
- Track click count for each link
- View all your links
- View stats for a specific link
- Delete your links

## Project Structure

    url_shortener/
    ├── app/
    │   ├── main.py          # Entry point
    │   ├── config.py        # Environment variables
    │   ├── routes/
    │   │   ├── auth.py      # Register and login
    │   │   ├── links.py     # Link management
    │   │   └── redirect.py  # URL redirect
    │   ├── models/
    │   │   ├── user.py      # User table
    │   │   └── link.py      # Link table
    │   ├── schemas/
    │   │   ├── auth.py      # Auth request/response shapes
    │   │   └── link.py      # Link request/response shapes
    │   ├── db/
    │   │   ├── database.py  # Database connection
    │   │   └── init_db.py   # Table creation
    │   └── utils/
    │       └── security.py  # JWT and password helpers
    ├── .env                 # Secrets (not pushed to GitHub)
    ├── requirements.txt
    └── README.md


## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/surajmahamunigit/url-shortener.git
cd url-shortener
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
DATABASE_URL=sqlite:///./url_shortener.db


### 5. Run the application
```bash
uvicorn app.main:app --reload
```

### 6. Open API docs
http://127.0.0.1:8000/docs


## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | /register | No | Register a new user |
| POST | /login | No | Login and get JWT token |
| POST | /links/shorten | Yes | Shorten a URL |
| GET | /links/my-links | Yes | Get all your links |
| GET | /links/stats/{short_code} | Yes | Get stats for a link |
| DELETE | /links/{short_code} | Yes | Delete a link |
| GET | /{short_code} | No | Redirect to original URL |
