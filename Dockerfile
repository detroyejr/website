## Flask Image
FROM python:3.7.0-slim

RUN apt-get update && apt-get install -y pandoc
## Add requirements
COPY app/requirements.txt requirements.txt
RUN pip install -r requirements.txt


ENV FLASK_APP=app/app.py
ENV FLASK_DEBUG=1
COPY app app

ENTRYPOINT [ "python" ]
CMD ["app/app.py"]