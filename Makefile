.PHONY: init
init:
	@poetry shell

.PHONY: setup
setup:
	@cp -Rf ./contrib/env-sample .env
	@poetry install

.PHONY: serve
serve:
	@python manage.py runserver

.PHONY: docs
docs:
	@cd docs && mkdocs serve

migrate:
	@python manage.py migrate

makemigrations:
	@python manage.py makemigrations

.PHONY: docker-run
docker-run:
	@docker-compose up -d --build

.PHONY: docker-destroy
docker-destroy:
	@echo "Destroying containers and volumes..."
	@docker-compose rm -vsf studybud studybud-db
	@docker volume rm studybud_postgres_data
