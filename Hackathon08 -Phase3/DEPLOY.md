# 🚀 Deployment Guide

This guide will help you deploy the **MyTodoApp** (TaskFlow) to the cloud.

## 1. Backend Deployment (Hugging Face Spaces)

We will deploy the FastAPI backend using Docker on Hugging Face Spaces.

1.  **Create a New Space**:
    *   Go to [huggingface.co/spaces](https://huggingface.co/spaces).
    *   Click **"Create new Space"**.
    *   **Name**: `mytodo-backend` (or similar).
    *   **License**: `MIT` (or your choice).
    *   **SDK**: Select **Docker**.
    *   **Public/Private**: Public is easier for testing, Private requires adding a token to the frontend. Go with **Public** for now.

2.  **Upload Code**:
    *   You can clone the Space repo and push your code, or upload files directly via the website.
    *   **Files to upload** (from the `backend/` folder):
        *   `src/` (folder)
        *   `Dockerfile`
        *   `requirements.txt`
        *   `init_db.py` (optional, if you need to run migration on the cloud, but since you are using Neon, your local migration already worked!)
    
    *   *Tip*: Using git is easiest.
        ```bash
        # Inside your local project root
        cd backend
        git init # if not already a separate repo
        git remote add space https://huggingface.co/spaces/YOUR_USERNAME/SPACE_NAME
        git add .
        git commit -m "Deploy backend"
        git push -f space main
        ```

3.  **Configure Environment Variables**:
    *   Go to your Space's **Settings** tab.
    *   Scroll to **Variables and secrets**.
    *   Add the following **Secrets** (for security):
        *   `DATABASE_URL`: `postgresql+asyncpg://...` (Your Neon Connection String)
        *   `GEMINI_API_KEY`: `sk-or-v1-...` (Your OpenRouter Key)
        *   `SECRET_KEY`: Generate a random string (e.g., `openssl rand -hex 32`).

4.  **Wait for Build**:
    *   The Space will build the Docker image. Once "Running", you will see your API URL (e.g., `https://yourusername-mytodo-backend.hf.space`).
    *   **Copy this URL**. You need it for the frontend.

---

## 2. Frontend Deployment (Vercel)

We will deploy the Next.js frontend to Vercel.

1.  **Push Frontend to GitHub**:
    *   Ensure your project is on GitHub. If you haven't committed the `frontend` folder yet, do so now.

2.  **Import to Vercel**:
    *   Go to [vercel.com](https://vercel.com).
    *   Click **"Add New..."** -> **"Project"**.
    *   Import your GitHub repository.

3.  **Configure Project**:
    *   **Root Directory**: Click "Edit" and select `frontend`.
    *   **Framework Preset**: Next.js (should auto-detect).
    *   **Environment Variables**: Add the following:
        *   `NEXT_PUBLIC_API_URL`: The Hugging Face Backend URL you copied (e.g., `https://yourusername-mytodo-backend.hf.space`). **Important:** Do NOT add a trailing slash `/`.
        *   `NEXT_PUBLIC_APP_URL`: The URL *this* deployment will have (e.g., `https://project-name.vercel.app`).
        *   `BETTER_AUTH_URL`: Same as `NEXT_PUBLIC_APP_URL` (e.g., `https://project-name.vercel.app`).
        *   `BETTER_AUTH_SECRET`: A random string (can be the same as backend SECRET_KEY).
        *   `DATABASE_URL`: Your Neon connection string (e.g., `postgresql+asyncpg://...`). **Critical:** The frontend needs this to perform authentication checks!

4.  **Deploy**:
    *   Click **"Deploy"**.

5.  **Finalize**:
    *   Once deployed, copy the final Vercel URL.
    *   Go back to Vercel Settings -> Environment Variables.
    *   Update `BETTER_AUTH_URL` to your actual Vercel URL (e.g., `https://project-name.vercel.app`).
    *   **Redeploy** (Go to Deployments -> Redeploy) to apply the change.

---

## 3. Connecting the Dots

1.  **CORS**:
    *   The backend currently allows all origins (`*`) which is fine for the hackathon.
    *   For strict security later, go to your Hugging Face Space Settings and set a variable `BACKEND_CORS_ORIGINS` to your Vercel URL.

2.  **Database**:
    *   Since you are using Neon (cloud DB), both your local machine, the Hugging Face backend, and the Vercel frontend (if it connects directly via Better Auth) will all talk to the same data source. Seamless!

**Enjoy your live TaskFlow app! 🚀**
