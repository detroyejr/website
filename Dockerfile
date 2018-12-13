## Python Image.
FROM python:3.7.1-alpine

## Add Packages.
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY app /app
CMD ["gunicorn", "--bind", ":8000", "app.app:app", "--access-logfile '-'"]