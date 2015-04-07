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
RUN apt-get install -y postgresql postgresql-contrib libpq-dev

# Add the source code
RUN mkdir -p /app
WORKDIR /app
ADD . /app/

# Move Sentry config to default location
ADD sentry.conf.py /.sentry/sentry.conf.py

# Install sentry and PostgreSQL binding
RUN pip install -r /app/requirements.txt

# Expose configured Sentry port
EXPOSE 3000
