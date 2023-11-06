FROM ubuntu:23.10
LABEL maintainer="svmitin@outlook.com"
SHELL ["/bin/bash", "-c"]

ENV LANG en_US.UTF-8
RUN apt -q update && \
    apt install -y software-properties-common locales apt-utils iputils-ping nmap htop i2pd yggdrasil wget && \
    locale-gen en_US.UTF-8 && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y --no-install-recommends python3.11 python3-pip python3.11-venv nodejs npm && \
    wget -O i2pd_2.47.0-1kinetic1_amd64.deb https://github.com/PurpleI2P/i2pd/releases/download/2.47.0/i2pd_2.47.0-1kinetic1_amd64.deb && \
    apt install -y --no-install-recommends /i2pd_2.47.0-1kinetic1_amd64.deb && \
    rm /i2pd_2.47.0-1kinetic1_amd64.deb && \
    python3 -m pip install --upgrade pip --break-system-packages

COPY . /app/
WORKDIR /app
RUN python3 -m venv /venv

RUN /venv/bin/pip --disable-pip-version-check install -r requirements.txt && \
    rm -rf /app/*

EXPOSE 80
