FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /project
WORKDIR /project
COPY . /project/
RUN pip install -r requirements.txt

