.PHONY: up down logs run migrate

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

run:
	.venv/Scripts/python.exe manage.py runserver

migrate:
	.venv/Scripts/python.exe manage.py migrate

activate:
	powershell.exe -NoExit -ExecutionPolicy Bypass -Command ". .\.venv\Scripts\Activate.ps1"