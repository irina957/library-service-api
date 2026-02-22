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

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone https://github.com/irina957/library-service-api.git
cd library-service-api
```

**2. Set up a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables:**

Create a `.env` file in the root directory based on `.env.sample`:

**5. Run migrations and start the server:**
```bash
python manage.py migrate
python manage.py runserver
```

## API & Telegram Notifications

When a user successfully creates a borrowing via `POST /api/borrowings/`, the Telegram bot immediately sends a notification:
```
New borrowing created!
- User: user@example.com
- Book: SampleBook
- Expected return: 2026-03-10
```