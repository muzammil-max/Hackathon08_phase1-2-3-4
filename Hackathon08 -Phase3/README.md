# MyTodoApp — Web Expansion

A secure, multi-user full-stack web application for task management.

## Tech Stack
- **Frontend**: Next.js 14 (App Router), TailwindCSS, Sonner (Toasts)
- **Backend**: FastAPI (Python), SQLModel, PostgreSQL
- **Auth**: JWT (JSON Web Tokens)

## Prerequisites
- Node.js 18+
- Python 3.10+
- PostgreSQL (or Neon.tech account)

## Setup & Running

### 1. Backend
```bash
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# Unix/macOS
source venv/bin/activate

pip install -r requirements.txt

# Configure environment
cp .env.example .env # Or create manually
# In .env:
# DATABASE_URL=postgresql+asyncpg://user:password@localhost/mytodo_db
# SECRET_KEY=your_random_secret_key

# Run the server
uvicorn src.main:app --reload
```

### 2. Frontend
```bash
cd frontend
npm install

# Configure environment
cp .env.local.example .env.local
# In .env.local:
# NEXT_PUBLIC_API_URL=http://localhost:8000

# Run the development server
npm run dev
```

## Features
- **User Authentication**: Secure signup and login.
- **Private Tasks**: Each user has their own private task list.
- **Task Management**: Create, Read, Update, Delete, and Toggle completion.
- **Responsive Design**: Works on mobile and desktop.
- **Real-time Feedback**: Toast notifications for user actions.