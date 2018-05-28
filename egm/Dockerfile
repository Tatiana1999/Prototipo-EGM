FROM ubuntu:14.04

MAINTAINER buho_team "sistemas@buho.media"

ENV LAST_UPDATED 2018-05-24

# Setup apt
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update

RUN DEBIAN_FRONTEND=noninteractive apt-get -qq install -y -u python nano curl wget dpkg python-dev python-setuptools git-core python-pip build-essential python-psycopg2 libpq-dev


#install requirements
ADD requirements.txt /egm/requirements.txt

#install requirements
ADD requirements.txt /egm/requirements.txt
RUN pip install -r /egm/requirements.txt

WORKDIR /egm
