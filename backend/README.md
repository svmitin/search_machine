# Freedom Search Backend

## Getting started

### Starts Django server on localhost
First you needly install Postgres
 - Create database `freedom`
 - Create os environment variables. You can make this on ~/.zshrc
```
export FREEDOM_DB_HOST="127.0.0.1"
export FREEDOM_DB_NAME="freedom-database-name"
export FREEDOM_DB_USER="freedom-database-user"
export FREEDOM_DB_PASS="freedom-database-password"
export FREEDOM_DB_PORT="5432"
```

Run project
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Run tests
```
python manage.py test
```

### Starts with Docker
```
docker-compose build backend
docker-compose up -d
```

## License
BSD 2-Clause License

## Project status
Active
