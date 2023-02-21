FROM python:3.8-slim-buster

# for flask web server
EXPOSE 8081

# set working directory
ADD . /app
WORKDIR /app

# install required libraries
RUN pip3 install -r requerimientos.txt

# This is the runtime command for the container
CMD python3 app.py
