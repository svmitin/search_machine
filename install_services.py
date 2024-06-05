import os


WORK_DIR = os.getcwd()


def install_service(service_name: str, service_file_content: str) -> None:
    with open(f'/etc/systemd/system/{service_name}', 'w') as f:
        f.write(service_file_content)
    print(f'installed new service-file: /etc/systemd/system/{service_name}')
    os.popen('sudo systemctl daemon-reload')
    os.popen(f'sudo systemctl enable {service_name}')


install_service('crawler.service', f'''
[Unit]
Description=crawler
After=network.target

[Service]
User=root
WorkingDirectory={WORK_DIR}
ExecStart={WORK_DIR}/venv/bin/python3 {WORK_DIR}/crawler/bot.py --start_url=https://i2pd.i2p
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')

install_service('backend.service', f'''
[Unit]
Description=backend
After=network.target

[Service]
User=root
WorkingDirectory={WORK_DIR}
ExecStart={WORK_DIR}/venv/bin/python3 {WORK_DIR}/backend/manage.py runserver
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
''')
