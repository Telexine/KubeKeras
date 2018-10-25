FROM python:3.6




ADD requirements.txt /usr/src/app/
WORKDIR /usr/src/app

RUN pip install -r requirements.txt 
RUN pip install git+https://www.github.com/keras-team/keras-contrib.git

ADD . /usr/src/app
EXPOSE 5000
RUN mkdir -p upload
RUN mkdir -p conv

CMD [ "python", "colorize.py" ]