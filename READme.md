
requirements:
asgiref==3.8.1
black==24.4.2
click==8.1.7
colorama==0.4.6
Django==5.0.6
mypy-extensions==1.0.0
packaging==24.0
pathspec==0.12.1
platformdirs==4.2.2
sqlparse==0.5.0
tzdata==2024.1

Activate Project 
1. clone repository

2. Create Virtual env 
Bash:
    python venv .venv

3. Activate env
Bash:
    .venv/bin/activate

4. install dependencies
Bash:
    pip install -r requirememts.txt

5. Apply Migrationms
Bash:
    python manage.py migrate 
    >
    python manage.py makemigrations

6. Create superusert
Bash:
    python manage.py createsuperuser

7. Hit the lights!@ 
Bash: 
    python manage.py runserver

8.  check local development server, create a user and try the logout
    -the blog app has the same issues
