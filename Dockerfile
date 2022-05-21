FROM debian:11
FROM python:3.10.4-slim-buster

WORKDIR /Team7Scanner/

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
CMD ["python3.10", "-m", "Team7"]
