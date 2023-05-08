FROM ubuntu:22.10
LABEL maintainer="svmitin@outlook.com"
SHELL ["/bin/bash", "-c"]

ENV LANG en_US.UTF-8
RUN apt -q update && \
    apt install -y software-properties-common locales apt-utils iputils-ping nmap htop i2pd yggdrasil && \
    locale-gen en_US.UTF-8 && \
    apt install -y --no-install-recommends python3 python3-pip nodejs npm && \
    wget -O i2pd_2.47.0-1kinetic1_amd64.deb https://github.com/PurpleI2P/i2pd/releases/download/2.47.0/i2pd_2.47.0-1kinetic1_amd64.deb && \
    apt install -y --no-install-recommends /i2pd_2.47.0-1kinetic1_amd64.deb && \
    rm /i2pd_2.47.0-1kinetic1_amd64.deb && \
    python3 -m pip install --upgrade pip

COPY . /app/
WORKDIR /app

RUN pip3 --disable-pip-version-check install -r requirements.txt && \
    rm -rf /app/*

EXPOSE 80
