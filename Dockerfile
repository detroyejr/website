## Python Image.
FROM python:3.7.1-alpine

## Add Packages.
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir

ENV FLASK_APP=app/app.py
COPY app /app

CMD ["gunicorn", "--bind", ":80", "app.app:app"]