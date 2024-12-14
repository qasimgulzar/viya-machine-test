FROM python:3.12.0-alpine3.18

WORKDIR /opt/project

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add gcc python3-dev libc-dev linux-headers
RUN apk add postgresql-client build-base postgresql-dev

COPY . .
RUN make base-requirements

EXPOSE 8000