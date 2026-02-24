FROM python:3.12-slim
LABEL maintainer="irakirvas78@gmail.com"
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser \
   --disabled-password \
   --no-create-home \
   django-user
USER django-user
