FROM nginx:latest
RUN mkdir /api

RUN apt update -y && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY src/ /api/
COPY production/server/nginx.conf /etc/nginx/nginx.conf
COPY production/start_api.sh /etc/start_api.sh

EXPOSE 80
ENTRYPOINT [ "/etc/start_api.sh" ]
