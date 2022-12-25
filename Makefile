configure:
	docker-compose down
	docker-compose up -d postgres
	docker-compose up -d nginx
	docker-compose build backend
	docker-compose up -d backend
	docker-compose exec backend python3 manage.py makemigrations
	docker-compose exec backend python3 manage.py migrate

destroy:
	docker-compose down --remove-orphans
	-docker volume rm freedom-postgres-data
	-docker rmi backend:latest
	-docker rmi frontend:latest
	-docker rmi spyder_1:latest
	-docker rmi spyder_2:latest
	-docker rmi spyder_3:latest
	-docker rmi nginx:latest
	-docker rmi postgres:14
	rm backend/search/migrations/0*.py

down:
	docker-compose down

run_backend:
	docker-compose up -d backend

run_spyders:
	docker-compose up -d backend
	docker-compose up -d spyder_1
	docker-compose up -d spyder_2
	docker-compose up -d spyder_3

migrate:
	docker-compose up -d backend
	docker-compose exec backend python3 manage.py makemigrations
	docker-compose exec backend python3 manage.py migrate

admin:
	docker-compose up -d backend
	docker-compose exec backend python3 manage.py createsuperuser

psql:
	docker-compose exec postgres psql -U django -b freedom

ps:
	docker-compose ps

df:
	docker system df
