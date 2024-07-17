### Запуск проекта локально:

Склонируйте проект и перейдите в директорию automatica_project
``` 
git clone git@github.com:goaho7/automatica_project.git 
``` 
``` 
cd automatica_project 
``` 

В директории где находится файл ".env.example" создайте файл ".env" и заполните его
в соответствии с ".env.example" своими данными подключения к бд PostgreSQL


Выполните команды
``` 
poetry install 
``` 
``` 
poetry shell 
``` 

перейдите в каталог с файлом manage.py
``` 
cd src 
``` 

Запустите миграции
``` 
python manage.py migrate 
``` 

Создайте суперюзера
``` 
python manage.py createsuperuser 
```

Запустите проект
``` 
python manage.py runserver 
``` 
