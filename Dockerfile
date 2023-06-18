FROM python:3.8-slim

WORKDIR /QACloudCamp

COPY requirements.txt .
COPY ./tests ./tests

RUN pip install -r requirements.txt

CMD python -m pytest -v