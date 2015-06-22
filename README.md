# ![](https://gravatar.com/avatar/11d3bc4c3163e3d238d558d5c9d98efe?s=64) aptible/sentry

[![Docker Repository on Quay.io](https://quay.io/repository/aptible/sentry/status)](https://quay.io/repository/aptible/sentry)

Sentry Docker image, deployable as an Aptible app.

## Installation and Usage

To run as an app on Aptible:

1. Provision a PostgreSQL database, either from the Aptible Dashboard or the Aptible CLI.

1. Configure the following (required and optional) environment variables for your Sentry app:

    | Variable | Description | Required? | Default Value |
    | -------- | ----------- | --------- | ------------- |
    | `ADMIN_PASSWORD` | Admin password | Yes | - |
    | `DATABASE_URL` | PostgreSQL database URL | Yes | - |
    | `SENTRY_URL_PREFIX` | Base URL for server | Yes | - |
    | `ADMIN_USERNAME` | Admin username for Sentry | No | `aptible` |
    | `TEAM_NAME` | Team name | No | `Aptible` |
    | `SECRET_KEY` | Secret key for [DSN clients](http://raven.readthedocs.org/en/latest/config/#the-sentry-dsn) sending events | No | (random) |
    | `SENTRY_KEY` | Sentry key | No | (random) |
    | `GITHUB_APP_ID` | GitHub OAuth application ID (for GitHub integration) | No | - |
    | `GITHUB_API_SECRET` | GitHub API secret | No | - |
    | `SSLIFY_DISABLE` | Disable forced HTTPS redirection? | No | `False` |
    | `MAILGUN_SERVER_NAME` | Your email domain (eg yourcompany.com) | No | - |
    | `MAILGUN_ACCESS_KEY` | Mailgun API Key | No | - |

1. Clone this repository and push it to your Aptible app:

    ```shell
    git clone https://github.com/aptible/docker-sentry.git
    cd docker-sentry
    git remote add aptible git@beta.aptible.com:YOUR_APP_HANDLE.git
    git push aptible master
    ```

You should be up and running now. If you're new to Sentry, try checking out the
[official documentation](http://sentry.readthedocs.org/en/latest/).

## Contributors

Very special thanks to Ozan Onay ([@ozan](https://github.com/ozan)) for implementing the Dockerized distribution of Sentry which we've released with minor modifications in this repo.

## Copyright and License

MIT License, see [LICENSE](LICENSE.md) for details.

Copyright (c) 2015 [Aptible](https://www.aptible.com) and contributors.

[<img src="https://s.gravatar.com/avatar/f7790b867ae619ae0496460aa28c5861?s=60" style="border-radius: 50%;" alt="@fancyremarker" />](https://github.com/fancyremarker)
