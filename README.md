Для запуска необходимо:
1) Клонировать репозиторий (дать команду в Git: git clone https://github.com/A-Sergey/Django-shop.git)
2) Создать виртуальное окружение.
Windows: - в cmd.exe перейти в папку клонированного проект
		 - ввести команду python -m venv название_окружения
		 - для запуска вируального окружения ввести команду 
		путь_проект\название_окружения\Script\activate.bat
		 - установить необходимые библиотеки для проекта, ввести команду
		 pip install -r requirements.txt
Linux:   - в console перейти в папку клонированного проект
		 - ввести команду python3 -m venv название_окружения
		 - для запуска вируального окружения ввести команду 
		source путь_проект\название_окружения\bin\activate
		 - установить необходимые библиотеки для проекта, ввести команду
		 pip install -r requirements.txt
3) Запустить миграцию командами
Windows:
		 - manage.py makemigrations
		 - manage.py migrate
Linux:
		 - python3 manage.py makemigrations
		 - python3 manage.py migrate
4) Запуск сервера командой
Windows:
		 - manage.py runserver
Linux:
		 - python3 manage.py runserver
4) Для тестового просмотра можно скачать готовую БД 
https://drive.google.com/file/d/1iBwzWdnFNuTiu_imnqByCEqJcUHewXiY/view?usp=sharing
		 