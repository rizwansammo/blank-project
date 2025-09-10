# Django Portfolio App

A personal portfolio website built with Django, PostgreSQL, and Bootstrap. Features include:
- Homepage, About, Projects, Blog, and Contact pages
- Admin-managed profile, skills, projects, posts, profile photo, and resume upload
- Blog with public read and admin CRUD
- Contact form that sends email via SMTP
- Responsive, SEO-friendly templates
- Dev and Prod settings

## Quickstart

1) Create virtual environment and install dependencies:
```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2) Configure environment:
- Copy .env.example to .env and edit values

3) Database:
- Create a PostgreSQL database (e.g., portfolio_db)
- Run migrations
```
python manage.py migrate
```

4) Create admin user:
```
python manage.py createsuperuser
```

5) Run server:
```
python manage.py runserver
```

Open http://127.0.0.1:8000/ and the admin at http://127.0.0.1:8000/admin/

## Admin Content

- Profile and Skills in the "Core" section
- Projects in the "Projects" section
- Posts in the "Blog" section

Upload your profile image and resume via the Profile admin.

## Production

- Set ENV=prod and configure DATABASE_URL, SECRET_KEY, ALLOWED_HOSTS, and SMTP vars.
- Use `Procfile` with Gunicorn.
- `whitenoise` serves static files (run collectstatic in prod).

```
python manage.py collectstatic --noinput
```

## Contact Email

Configure SMTP via env variables in `.env`:
- EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS, DEFAULT_FROM_EMAIL

In development, dev settings use console email backend. In production, `prod.py` relies on SMTP settings.

## License

MIT