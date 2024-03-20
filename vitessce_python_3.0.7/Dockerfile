FROM python:3.12

RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

COPY requirements.txt /requirements.txt

RUN /root/.cargo/bin/uv pip install --system --no-cache -r requirements.txt