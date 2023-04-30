def get_site_metric_code(site_hash: str) -> str:
    """Возвращает JS код интеграции метрики"""
    # TODO: сейчас мы просто отправляем на сервер информацию о продолжительности присутствия на сайте.
    # возможно стоит дописать код, чтобы на странице отображалась информация о популярности сайта.
    # разумеется количество уникальных пользователей мы замерять не можем и не будем.

    # TODO: скрипт не тестировался
    return f'''
    <script>
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "https://freedom.i2p/metrics", false);
    xhr.setRequestHeader("Content-Type", "application/json");
    unique_str = String(new Date()) + String(Math.random());
    let hash = 0;
    for (i = 0; i < unique_str.length; i++) {{
        char = unique_str.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }}
    for (let i = 0; i < 5; i++) {{
        let data = {{
            "user_hash": String(hash),
            "site_hash": "{site_hash}"
        }};
        xhr.send(data);
        sleep(1000 * i);
    }}
    </script>
    '''
