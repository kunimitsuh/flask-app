# pull official base image
FROM python:3.8.1-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# set work directory
WORKDIR /usr/src/app

# copy project
COPY ./app .

ENV PORT 8080

CMD ["gunicorn", "run:app", "--config=config.py"]