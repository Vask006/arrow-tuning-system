# Deployment Guide

## Docker Compose (Quick Start)

```bash
cd docker
docker-compose up -d
```

This starts:
- PostgreSQL with TimescaleDB
- Redis
- Backend API (port 8000)
- Frontend (port 3000)

## Production Deployment

### 1. Environment Configuration

Create `.env` files:

**backend/.env:**
```bash
SECRET_KEY=<generate-secure-key>
DATABASE_URL=postgresql+asyncpg://user:pass@host:5432/db
REDIS_URL=redis://host:6379/0
ENVIRONMENT=production
DEBUG=false
```

**frontend/.env:**
```bash
NEXT_PUBLIC_API_URL=https://api.yourdomain.com
```

### 2. Database Setup

```sql
-- Create database with TimescaleDB
CREATE DATABASE ats_db;
\c ats_db
CREATE EXTENSION IF NOT EXISTS timescaledb;
```

### 3. Backend Deployment

```bash
cd backend
pip install -e .
alembic upgrade head
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Frontend Deployment

```bash
cd frontend
npm install
npm run build
npm start
```

### 5. Reverse Proxy (nginx)

```nginx
server {
    listen 80;
    server_name api.yourdomain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Monitoring

- **Logs**: Check `logs/` directory
- **Metrics**: Access Prometheus at `:9090`
- **Health**: Check `/health` endpoint

## Backup

```bash
# Database backup
pg_dump -U ats_user ats_db > backup.sql

# Redis backup
redis-cli SAVE
```

## Security Checklist

- [ ] Strong SECRET_KEY configured
- [ ] HTTPS enabled
- [ ] Firewall rules configured
- [ ] Regular backups scheduled
- [ ] Monitoring alerts set up

