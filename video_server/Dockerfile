FROM python:3.8-alpine
RUN apk update && apk upgrade
RUN apk add --no-cache bash \
                       gcc \
                       python3-dev \
                       musl-dev 
                         
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
RUN pip3 install --upgrade pip setuptools
COPY requirements.txt /usr/src/app/requirements.txt
RUN cd /usr/src/app && pip install -r requirements.txt
COPY . /usr/src/app

