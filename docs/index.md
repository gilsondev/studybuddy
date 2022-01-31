
# Documentation of project Studybuddy

## Installation

- Clone this project
```shell
git clone git@github.com:gilsondev/studybud.git
```

- (Optional) Create a virtual environment
```shell
make init
```

- Install the dependencies
```shell
make setup
```

- Inicie os containers via docker-compose
```shell
docker-compose up -d
```

## Deploy

- Create the instances of _staging_ and _production_ of Heroku
```shell
heroku create instance-staging --remote staging
heroku create instance --remote production
```

- Prepare the environment with the commands below, using `-a <app-name>`
```shell
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=.herokuapp.com

# Configure o email com sendgrid
heroku addons:create sendgrid:starter
heroku config:set EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
heroku config:set EMAIL_HOST_USER=`heroku config:get SENDGRID_USERNAME`
heroku config:set EMAIL_HOST_PASSWORD=`heroku config:get SENDGRID_PASSWORD`
```

## Commands

* `make setup` - Prepare the environment project to develop
* `make docs` - Start the doc server
* `make serve` - Start the development server
* `make migrate` - Execute all migrations
* `make makemigrations` - Create new migrations
* `make docker-run` - Build and run all docker containers (app, db, etc)
* `make docker-destroy` - Destroy all containers and your volumes

## Project structure

```
.
├── conftest.py
├── contrib
│   ├── env-sample
│   └── secret_gen.py
├── docker-compose.yml
├── docs
│   ├── docs
│   │   └── index.md
│   └── mkdocs.yml
├── manage.py
├── pyproject.toml
├── poetry.lock
├── studybud
│   ├── asgi.py
│   ├── __init__.py
│   └── conftest.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── base
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests
│   └── views.py
├── Procfile
├── pytest.ini
└── README.md
```

## Other informations

To better understand of how works this documentation, access [mkdocs.org](https://mkdocs.org).
