install:
	docker-compose down
	docker-compose build sm_backend
	docker-compose up -d sm_backend
	docker-compose exec sm_backend python3 manage.py makemigrations
	docker-compose exec sm_backend python3 manage.py migrate
	docker-compose exec sm_backend python3 manage.py createsuperuser
	docker stop sm_backend
	docker stop sm_postgres
	docker stop sm_nginx

remove:
	-docker stop sm_spyder_1
	-docker stop sm_spyder_2
	-docker stop sm_spyder_3
	-docker stop sm_backend
	-docker stop sm_postgres
	-docker stop sm_nginx

	-docker volume rm search_machine_postgres-data
	-docker rmi sm_spyder_1:latest
	-docker rmi sm_spyder_2:latest
	-docker rmi sm_spyder_3:latest
	-docker rmi search_machine_sm_backend:latest
	-docker rmi sm_frontend:latest
	-docker rmi sm_postgres:13
	-docker rmi sm_nginx:latest

	rm backend/search/migrations/0*.py

down:
	-docker stop sm_spyder_1
	-docker stop sm_spyder_2
	-docker stop sm_spyder_3
	-docker stop sm_backend
	-docker stop sm_postgres
	-docker stop sm_nginx

run_backend:
	docker-compose up -d sm_backend

run_spyders:
	docker-compose up -d sm_spyder_1
	docker-compose up -d sm_spyder_2
	docker-compose up -d sm_spyder_3

migrate:
	docker-compose up -d sm_backend
	docker-compose exec sm_backend python3 manage.py makemigrations
	docker-compose exec sm_backend python3 manage.py migrate

admin:
	docker-compose up -d sm_backend
	docker-compose exec sm_backend python3 manage.py createsuperuser

psql:
	docker-compose exec sm_postgres psql -U django -b freedom

ps:
	docker-compose ps

df:
	docker system df
