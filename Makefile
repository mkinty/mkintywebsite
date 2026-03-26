# ==============================
# Variables
# ==============================

COMPOSE_DEV = docker compose -f docker-compose.dev.yml
COMPOSE_PROD = docker compose -f docker-compose.prod.yml

# ==============================
# Development
# ==============================

# Build images
build:
	$(COMPOSE_DEV) build

# Lancer containers dev
up:
	$(COMPOSE_DEV) up
	#$(COMPOSE_DEV) up -d

# Stop containers
down:
	$(COMPOSE_DEV) down

# Logs
logs:
	$(COMPOSE_DEV) logs -f

# Django commands
makemigrations:
	$(COMPOSE_DEV) exec web python manage.py makemigrations

migrate:
	$(COMPOSE_DEV) exec web python manage.py migrate

createsuperuser:
	$(COMPOSE_DEV) exec web python manage.py createsuperuser

collectstatic:
	$(COMPOSE_DEV) exec web python manage.py collectstatic

shell:
	$(COMPOSE_DEV) exec web python manage.py shell

# ==============================
# Tests
# ==============================

test:
	$(COMPOSE_DEV) exec web python manage.py test --keepdb

coverage:
	$(COMPOSE_DEV) exec web coverage run manage.py test
	$(COMPOSE_DEV) exec web coverage report

test-users:
	$(COMPOSE_DEV) exec web python manage.py test apps.users

test-auth:
	$(COMPOSE_DEV) exec web python manage.py test apps.authentication

# ==============================
# Documentation (MkDocs)
# ==============================

docs-init:
	$(COMPOSE_DEV) exec web mkdocs new docs

docs-serve:
	$(COMPOSE_DEV) exec web mkdocs serve -a 0.0.0.0:8001

docs-build:
	$(COMPOSE_DEV) exec web mkdocs build

docs-deploy:
	$(COMPOSE_DEV) exec web mkdocs gh-deploy

# ==============================
# Production
# ==============================

prod-build:
	$(COMPOSE_PROD) build

prod-up:
	$(COMPOSE_PROD) up -d

prod-down:
	$(COMPOSE_PROD) down

prod-logs:
	$(COMPOSE_PROD) logs -f

prod-migrate:
	$(COMPOSE_PROD) exec web python manage.py migrate

prod-collectstatic:
	$(COMPOSE_PROD) exec web python manage.py collectstatic --noinput