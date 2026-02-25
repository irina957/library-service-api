# 📚 Library Service API

A robust backend system for managing book borrowings. This project streamlines library operations by tracking inventory, managing user borrowings, and providing real-time notifications via Telegram.

## 🚀 Features

- **Book Management**: Full CRUD functionality for administrators to manage the book catalog (title, author, inventory, and daily rate).
- **Borrowing System**: Users can create borrowings which automatically decrease the book's inventory.
- **Return Logic**: A custom "return" action that calculates the return date and restores the book inventory.
- **Telegram Notifications**: Real-time alerts sent to a Telegram chat whenever a new borrowing is created.
- **Authentication & Security**:
  - Secured with **JWT (JSON Web Tokens)**.
  - Environment variables managed via `python-dotenv` to keep API keys private.
- **Filtering**: Advanced filtering for borrowings by user ID and active status.

---

## 🐳 Quick Start with Docker

1. **Clone the repository.**
2. **Create a `.env` file** based on `.env.sample`.
3. **Build and run the containers:**
```bash
   docker-compose up --build
```

> The system will automatically wait for the database, run migrations, and load sample book data.

4. **Access the API:**
   - API Root: `http://localhost:8000/api/`
   - Admin Panel: `http://localhost:8000/admin/`

5. **Create your own admin:**
```bash
   docker-compose exec app python manage.py createsuperuser
```

---

## 🤖 API & Telegram Notifications

When a user successfully creates a borrowing via `POST /api/borrowings/`, the Telegram bot immediately sends a notification:
```
New borrowing created!
- User: user@example.com
- Book: SampleBook
- Expected return: 2026-03-10
```