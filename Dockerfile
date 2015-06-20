FROM quay.io/aptible/ubuntu:14.04

# Set locales (for PostgreSQL)
RUN apt-get update && apt-get install -y language-pack-en
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
RUN locale-gen en_US.UTF-8

# Python/pip
RUN apt-get install -y build-essential python-dev python-pip

# PostgreSQL client libraries
RUN ln -s -f /bin/true /usr/bin/chfn
RUN apt-get install -y postgresql postgresql-contrib libpq-dev

# Add the source code
RUN mkdir -p /app
WORKDIR /app

# Install sentry and PostgreSQL binding
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app

# Move Sentry config to default location
RUN mkdir -p /root/.sentry/
ADD sentry.conf.py /root/.sentry/sentry.conf.py

# Expose configured Sentry port
EXPOSE 3000
