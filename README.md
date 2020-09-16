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

## Migration

To adjust updated model information, migration should be done propetly

Follow steps are describing how to migrate via Django framework

### 1. Create migrations

```bash
# This commend will generate migration files under app/migrations directory
# It will only be happened when models have any changes
python manage.py makemigrations
```

### 2. Check SQL (optional)

```bash
# If you want to check SQL for specific migration file
# You can use below command. It's not necessay to migrate properly
python manage.py sqlmigrate app $NUMBER_OF_MIGRATION_FILE
```

### 3. Do migration

```bash
python manage.py migrate
```

While doing migration you might need to use few command to handle it
Here's few tips to handle it in case.

### Show migration status

```bash
python manage.py showmigration
```

### Way to reset migration

```bash
# This is only recommended for development env or
# when you can sure that you don't have important data

# Remove database first.
rm -rf ./db.sqlite3

# Make it empty migrations directory except `__init__.py`
# If you removed `__init__.py`, you just need to create new file with same name but empty content.
rm -rf ./app/migrations/** && touch ./app/migrations/__init__.py

# Now you can check status of migration
python manage.py showmigration
```

## Authors

> Jay Lee <jaylee.possible@gmail.com>

> Gingcheong <gincheong2@gmail.com>
