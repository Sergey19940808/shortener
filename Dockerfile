FROM python:3.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip3 install --upgrade pip
RUN pip3 install pipenv

COPY ./Pipfile /code/Pipfile

RUN pipenv install --system --deploy --skip-lock --dev

COPY . /code/
