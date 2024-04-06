FROM python:3.12.0

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY project /app/project

CMD ["python","project/manage.py","runserver", "0.0.0.0:8000"]

EXPOSE 8000