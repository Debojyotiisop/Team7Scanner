FROM debian:11
FROM python:3.10.4-slim-buster

WORKDIR /Team7Scanner/

RUN apt-get update && apt-get upgrade -y

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install -U -r requirements.txt
COPY . .
CMD ["python3.10", "-m", "Team7"]
