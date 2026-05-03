# Render.com Deployment Guide

## Prerequisites
- GitHub account with this repository
- Render.com account
- MongoDB Atlas connection string

## Steps to Deploy

### 1. Prepare MongoDB
- Create a MongoDB Atlas cluster (if not already done)
- Get your connection string (MONGODB_URL)

### 2. Push to GitHub
```bash
git add .
git commit -m "Prepare for Render deployment"
git push origin main
```

### 3. Deploy on Render.com
1. Go to [render.com](https://render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in the details:
   - **Name**: `url-shortener` (or your preferred name)
   - **Runtime**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Set Environment Variables:
   - **MONGODB_URL**: Your MongoDB connection string
   - **BASE_URL**: Your Render domain (e.g., `https://url-shortener-xxxx.onrender.com`)
6. Click "Deploy"

## Environment Variables Required
- `MONGODB_URL`: MongoDB connection string
- `BASE_URL` (optional): Base URL for shortened links (auto-detected on Render if not set)

## Files Added for Render Deployment
- `render.yaml`: Infrastructure configuration for Render
- `Procfile`: Process file for Render (backup configuration)

## Notes
- The app automatically binds to `0.0.0.0` and uses the PORT environment variable
- Ensure MongoDB connection string is kept secure in Render environment variables
- The app uses Jinja2 templates from the `views/` directory
- MongoDB database should be configured to accept connections from Render's IP ranges
