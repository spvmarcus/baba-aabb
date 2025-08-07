https://joegsuero.medium.com/django-unpacked-the-structure-every-developer-should-know-part-3-b715a0ada24a

project_root/
├── config/ # Main project configuration and root URLs
│ ├── settings/ # Environment-specific settings files
│ │ ├── **init**.py # Assembles settings (e.g., imports base + environment)
│ │ ├── base.py # Common configuration for all environments
│ │ ├── development.py # Development-specific config
│ │ └── production.py # Production-specific config
│ ├── urls.py # Project root URLs
│ ├── wsgi.py # WSGI configuration
│ └── asgi.py # ASGI configuration (if using async/websockets)
├── apps/ # Directory for all custom apps (our business logic)
│ ├── core/ # App for cross-cutting concerns (users, global config, utilities)
│ │ ├── migrations/
│ │ ├── templates/ # Templates
│ │ ├── tests/ # Test structure within the app
│ │ │ ├── **init**.py
│ │ │ ├── test_models.py
│ │ │ ├── test_views.py
│ │ │ ├── test_managers.py
│ │ │ └── test_services.py # If using service layer
│ │ ├── **init**.py
│ │ ├── admin.py
│ │ ├── apps.py
│ │ ├── models.py
│ │ ├── managers.py
│ │ ├── services.py
│ │ ├── forms.py
│ │ ├── urls.py # App-specific URLs
│ │ ├── views.py
│ │ └── services.py # Business logic layer (optional but recommended)
│ └── <other_app>/ # E.g.: products, orders, payments, etc.
│ ├── ... (similar internal structure)
├── staticfiles/ # Collected static files (for production)
├── mediafiles/ # User-uploaded files (for production)
├── templates/ # Base project templates (layouts, errors)
├── requirements/ # Dependency requirements
│ ├── base.txt # Common dependencies
│ ├── development.txt # Development dependencies (e.g., debug toolbar, testing)
│ └── production.txt # Production dependencies (e.g., gunicorn, sentry)
├── scripts/ # Useful scripts for deploy, setup, etc.
├── locale/ # Translation files (i18n)
├── .env.example # Environment variables template
├── manage.py # Main management script
└── Dockerfile # Optional but very common for deployment
