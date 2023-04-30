# Поисковая система Freedom

![Поисковая система Freedom. Главная страница](https://user-images.githubusercontent.com/69031401/235291923-0e5e8436-7605-4b05-8f51-74893a8837f3.png)

В настоящий момент нет инструкции по ручному локальному развертыванию проекта, 
а так-же деплою на VPS или использованию с Kubernetes. Только локальный запуск в Docker для разработки.

## Текущая стадия развития. Backlog

Проект в состоянии MVP. Он работает, но нуждается в следующих доработках для запуска в продакшн:
* ✅ добавление возможности для пользователей/SEO-специалистов ручного добавления сайтов в очередь индексации (с выдачей JS-кодов метрик)
* 🔺 нужны алгоритмы ранжирования поисковой выдачи на основе предыдущего шага
* 🔺 повторная индексация уже посещенных страниц для обновления информации
* 🔺 переориентирование поисковой системы на работу в [i2p](https://ru.wikipedia.org/wiki/I2P) ([i2pd](https://i2pd.website/) роутер) и/или [yggdrasil](https://ru.wikipedia.org/wiki/Yggdrasil) сетях
* добавление локализации для пользователей не знающих русский язык
* добавление возможности деплоя на VPS посредством [Ansible](https://ru.wikipedia.org/wiki/Ansible)
* по неизвестной причине через какое-то время сетевые краулеры перестают работать (зависают)
* нет уверенности, что полнотекстовый поиск будет работать при большом объеме данных в PostgreSQL
* контейнер с Vue.js не отслеживает изменения в коде. Делает сборку и завершает работу
* приложение Vue.js криво работает с урлами. Загрузка возможна только с корня. Нельзя открыть страницу по любому другому URL
* возможно API-endpoint метрик стоит переписать на Golang. При частом поступлении информации от JS-кода интеграции метрик могут возникнуть трудности с производительностью

## Структура проекта

- __backend/__ - Бэкэнд часть поисковой системы. Предоставляет API и административную панель. Приложение реализовано на Django
    - __freedom/__ - Директория конфигурации Django. Здесь хранятся параметры доступа к БД, перечень доступных урлов, файл настроек Django
    - __search/__ - Основные файлы backend-проекта. Модели, вьюхи, настройки админки
    - __static/__ - Статические файлы административной панели. В теории их здесь быть не должно, но для простоты развертывания проекта они добавлены
    - __manage.py__ - Точка входа приложения Django. Все Django-команды выполняются через этот скрипт
- __deploy/__ - Скрипты для развертывания проекта в Docker для нужд разработки. Возможно здесь в будущем появятся скрипты Ansible для деплоя на VPS
- __frontend/__ - Браузерное веб-приложение. Написано на Vue.js 3 версии
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

**Примечания**
* В если в файле `backend/search/migrations/0001_initial.py` будет изменена только дата, 
данные изменения следует отменить

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

## License
BSD 2-Clause License

## Project status
Active