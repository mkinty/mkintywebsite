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
	$(COMPOSE_DEV) up -d

# Stop containers
down:
	$(COMPOSE_DEV) down

# Logs
logs:
	$(COMPOSE_DEV) logs -f

# Django commands
makemigrations:
	$(COMPOSE_DEV) exec web python src/manage.py makemigrations

migrate:
	$(COMPOSE_DEV) exec web python src/manage.py migrate

createsuperuser:
	$(COMPOSE_DEV) exec web python src/manage.py createsuperuser

collectstatic:
	$(COMPOSE_DEV) exec web python src/manage.py collectstatic --noinput

shell:
	$(COMPOSE_DEV) exec web python src/manage.py shell

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
	$(COMPOSE_PROD) exec web python src/manage.py migrate

prod-collectstatic:
	$(COMPOSE_PROD) exec web python src/manage.py collectstatic --noinput