# Using python alpine build version 3.7
FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

# Installing additional libraries required for linux and postgres
RUN apk add --no-cache --update \
    build-base \
    postgresql-dev \
    bash \
    && rm -rf /var/cache/apk/*

# Change in to the working directory in the container
RUN mkdir /app
WORKDIR /app

# Copy and install the requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r /requirements.txt
