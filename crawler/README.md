# Freedom Search crawler Bot

## Getting started

### Starts Django server on localhost
First you needly install Postgres
 - Create database `freedom`
 - Create os environment variables. You can make this on ~/.shrc
```
FREEDOM_DB_HOST="127.0.0.1"
FREEDOM_DB_NAME="freedom-database-name"
FREEDOM_DB_USER="freedom-database-user"
FREEDOM_DB_PASS="freedom-database-password"
FREEDOM_DB_PORT="5432"
```

Run project
При первом запуске всегда нужно указать URL страницы с которой начнется обход
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 bot.py --start_url=https://petrosian.ru --crawler_name=crawler_1
```

Run tests
```
# TODO: wrong tests. Only checking currently installed venv
python test.py
```

### Starts with Docker
```
docker-compose build crawler
docker-compose up -d
```

## License
BSD 2-Clause License

## Project status
Active
