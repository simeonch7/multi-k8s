FROM python:3.8-slim-buster

WORKDIR "/app"

RUN ["apt-get", "update"]
RUN ["apt-get", "install", "-y", "vim"]
RUN ["apt-get", "install", "-y", "telnet"]

COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD tail -f /dev/null