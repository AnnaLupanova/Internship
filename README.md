## Getting started
Clone repo:
```
git clone <path_repo>
cd Internship
```

Edit file .env : specify the access details for the database in the file.
```
POSTGRES_USER="{YOUR_POSTGRES_USER}"
POSTGRES_PASSWORD="{YOUR_POSTGRES_PASSWORD}"
```

Run the application:
```
docker-compose up -d
```
Run commands below for migrate data:
```
docker exec -it web /bin/bash
python manage.py makemigrations
python manage.py migrate
```

API documentation:
- 127.0.0.1:8000/docs

