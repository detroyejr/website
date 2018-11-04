## Python Image.
FROM python:3.7.1-slim

## Add Packages.
COPY app/requirements.txt requirements.txt
RUN apt-get update \
    && apt-get install -y pandoc \
    && pip install -r requirements.txt

ENV FLASK_APP=app/app.py
COPY app app

ENTRYPOINT [ "python" ]
CMD ["app/app.py"]