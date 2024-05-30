# Поисковая система Freedom

![Поисковая система Freedom. Главная страница](https://user-images.githubusercontent.com/69031401/235291923-0e5e8436-7605-4b05-8f51-74893a8837f3.png)

В настоящий момент нет инструкции по ручному локальному развертыванию проекта, 
а так-же деплою на VPS или использованию с Kubernetes. Только локальный запуск в Docker для разработки.

## Текущая стадия развития. Backlog

Проект в состоянии MVP. Он работает локально в Docker и в продовой среде на VPS
Ближайшие планы
- краулер должен работать в многопоточном режиме

## Структура проекта

- __backend/__ - Бэкэнд часть поисковой системы. Предоставляет API и административную панель. Приложение реализовано на Django
    - __freedom/__ - Директория конфигурации Django. Здесь хранятся параметры доступа к БД, перечень доступных урлов, файл настроек Django
    - __search/__ - Основные файлы backend-проекта. Модели, вьюхи, настройки админки
    - __static/__ - Статические файлы административной панели. В теории их здесь быть не должно, но для простоты развертывания проекта они добавлены
    - __manage.py__ - Точка входа приложения Django. Все Django-команды выполняются через этот скрипт
- __docker/__ - Скрипты развертывания проекта в Docker для нужд разработки
- __crawler/__ - Сетевой краулер для обхода веб-страниц и их индексации. Написан на Python3 с использованием библиотек requests, BeautifulSoup, SQLAlchemy

Схему БД можно посмотреть перейдя по ссылке [https://app.quickdatabasediagrams.com/#/d/8PAdpn](https://app.quickdatabasediagrams.com/#/d/8PAdpn)
SWAGGER схема отсутсвует


## Локальный запуск с использованием Docker

Сборка и запуск проекта происходят в три шага:
* создание базового образа. Здесь же будут запрошены логин/пароль администратора
* запуск веб-сервера
* запуск сетевых краулеров
```
make install
make run_backend
make run_crawlers
```

Далее нужно внести изменения в файл `/etc/hosts`:
```ini
# SearchMachime
127.0.0.1       freedom
```

Для просмотра страницы нужно открыть URL [http://freedom:8000/](http://freedom:8000/) \
Административная панель [http://freedom:8000/admin](http://freedom:8000/admin)

## Команды Docker
```bash
make install        # Подготовить окружение
make remove         # Уничтожить все контейнеры. Работает с переменным успехом
make down           # Завершить все контейнеры
make run_backend    # Запускает бэкэнд приложение Django для API и Административной панели
make stop_backend   # Завершает бэкэнд приложение Django
make run_crawlers   # Запускает 3 сетевых краулера
make stop_crawlers  # Завершает работу сетевых краулеров
make migrate        # Выполняет миграции
make backup         # Завершает работу сетевых краулеров и создает дамп БД в файле `dump.sql`
make admin          # Регистрирует нового администратора
make psql           # Запускает утилиту psql
make ps             # Статус контейнеров
make df             # Проверить расход памяти
```

## Запуск в прод-среде

```bash
apt-get update && apt-get upgrade -y && apt-get install -y python3 python3-venv postgresql i2pd
service i2pd start
sudo -i -u postgres
createuser search_user
createdb machine -O search_user
psql
ALTER USER search_user WITH ENCRYPTED PASSWORD 'TpEaWwb(TA_[zSL@a2';
\q
exit

git clone git@github.com:svmitin/search_machine.git
cd search_machine
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
vim backend/freedom/constans.py
cd backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
cd ../
python3 install_services.py
```

## License
BSD 2-Clause License

## Project status
Active