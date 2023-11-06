install:
	docker-compose down
	docker-compose build sm_backend
	docker-compose up -d sm_backend
	docker-compose exec sm_backend /venv/bin/python3 manage.py makemigrations
	sleep 5
	docker-compose exec sm_backend /venv/bin/python3 manage.py migrate
	docker-compose exec sm_backend /venv/bin/python3 manage.py createsuperuser
	docker-compose exec sm_backend /venv/bin/python3 manage.py loaddata /app/backend/search/fixtures/categories.yaml
	docker stop sm_backend
	docker stop sm_postgres
	docker stop sm_nginx

remove:
	-docker stop sm_crawler_1
	-docker stop sm_crawler_2
	-docker stop sm_crawler_3
	-docker stop sm_backend
	-docker stop sm_postgres
	-docker stop sm_nginx

	-docker volume rm search_machine_postgres-data
	-docker rmi sm_crawler_1:latest
	-docker rmi sm_crawler_2:latest
	-docker rmi sm_crawler_3:latest
	-docker rmi search_machine_sm_backend:latest
	-docker rmi sm_frontend:latest
	-docker rmi sm_postgres:13
	-docker rmi sm_nginx:latest

	-rm backend/search/migrations/0*.py

down:
	-docker stop sm_crawler_1
	-docker stop sm_crawler_2
	-docker stop sm_crawler_3
	-docker stop sm_backend
	-docker stop sm_postgres
	-docker stop sm_nginx

x:
	docker-compose up -d sm_backend

stop_backend:
	docker-compose stop sm_backend
	docker-compose stop sm_frontend

run_crawlers:
	docker-compose up -d sm_crawler_1
	docker-compose up -d sm_crawler_2
	docker-compose up -d sm_crawler_3

stop_crawlers:
	docker-compose stop sm_crawler_1
	docker-compose stop sm_crawler_2
	docker-compose stop sm_crawler_3

migrate:
	docker-compose up -d sm_backend
	docker-compose exec sm_backend /venv/bin/python3 manage.py makemigrations
	docker-compose exec sm_backend /venv/bin/python3 manage.py migrate

backup:
	docker-compose up -d sm_backend
	-docker stop sm_crawler_1
	-docker stop sm_crawler_2
	-docker stop sm_crawler_3
	docker-compose exec sm_postgres pg_dump -U user machine > dump.sql

admin:
	docker-compose up -d sm_backend
	docker-compose exec sm_backend /venv/bin/python3 manage.py createsuperuser

psql:
	docker-compose exec sm_postgres psql -U django -b freedom

ps:
	docker-compose ps

df:
	docker system df
