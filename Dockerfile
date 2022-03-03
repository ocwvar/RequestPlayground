FROM python:3.7.8

WORKDIR /
COPY . ./

RUN pip install -r dependencies.txt
CMD ./runserver.sh