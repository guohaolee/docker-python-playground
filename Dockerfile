FROM python:3.7

WORKDIR /app

RUN apt-get update && apt-get install -y \
less \
vim \
cron \
vim \
curl \
nginx \
nano


EXPOSE 5000

ENTRYPOINT ["/app/dev/entrypoint.sh"]