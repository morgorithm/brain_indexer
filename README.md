# Brain Indexer

## About Brain Indexer

> Flash card WEB/APP for memorizing something by repeating

> powered by Django

## Initializing for Development ENV

### 1. Install python

### 2. Setup venv

```bash
python3 -m pip venv $VENV_NAME
```

### 3. Activate venv

```bash
source $VENV_NAME/bin/activate # for Unix / Mac
```

```powershell
$VENV_NAME/bin/activate.bat # for Windows
```

### 4. Install Django

```bash
pip install Django
```

### 5. Database migration

```bash
python manage.py migrate
```

### 6. Creating super user for Django admin [more info](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#introducing-the-django-admin)

```bash
python manage.py createsuperuser
```

### 7. Run server

```bash
# You can specify running port by appending port number at the end of this command
python manage.py runserver
```

## Authors

> Jay Lee <jaylee.possible@gmail.com>

> Gingcheong <gincheong2@gmail.com>
