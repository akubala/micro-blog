FROM python:3.8.6-slim-buster
WORKDIR /app
COPY . /app

RUN pip install -r requirements.cfg
ENV PYTHONUNBUFFERED 1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
