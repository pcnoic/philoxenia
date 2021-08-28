FROM node:current-slim AS buildclient
LABEL Maintainer="Christos Alexiou <christos@tynr.io>"
ENV project "philoxenia"

WORKDIR /gen

COPY client/ /gen
RUN npm install -g @quasar/cli
RUN npm install
RUN quasar build -m pwa

FROM nginx:latest AS buildapi
RUN mkdir /api

RUN apt update -y && apt upgrade -y

RUN apt install -y -q build-essential python3-pip python3-dev
RUN pip3 install -U pip setuptools wheel
RUN pip3 install gunicorn uvloop httptools

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

COPY src/ /api/
RUN ls -la /api
COPY --from=buildclient /gen/dist/pwa/ /usr/share/nginx/html/
RUN ls -la /usr/share/nginx/html
COPY production/server/reverse.conf /etc/nginx/conf.d/philoxenia.conf
COPY production/start_api.sh /etc/start_api.sh

EXPOSE 80
ENTRYPOINT [ "/etc/start_api.sh" ]
