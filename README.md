# Job Board API

Django REST Framework API for a job board platform — role-based access (candidates, employers, admins), advanced search, async email notifications, S3 file uploads, deployed on AWS.

## Stack
- Django 6 + DRF
- PostgreSQL 16
- Redis 7 + Celery (Week 2)
- Docker / Docker Compose
- AWS (EC2 + RDS + S3) — Week 2

## Local Setup
\`\`\`bash
cp .env.example .env
docker compose up --build
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py createsuperuser
\`\`\`

API: http://localhost:8000 · Admin: http://localhost:8000/admin

## Status
🚧 In development — Week 1 of 6
- [x] Day 1: Project skeleton, Docker, core models, admin
- [ ] Day 2: JWT auth, serializers, first API endpoints
- [ ] Week 1: Full CRUD, search, filtering, pagination
- [ ] Week 2: Celery, S3 uploads, AWS deployment, CI/CD