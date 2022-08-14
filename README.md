# **Django-shop**
---
В данном репозитории представлен тестовый проект интернет-магазина на Django.
В проекте реализован функционал регистрации/логин пользователей,
добавления/удаления товаров в корзину, написание комментарий к товару,
поиск товаров. В дальнейшем планируется улучшить верстку, функционал редактирования написаных комментарий.


### **Для запуска необходимо:**
1. Клонировать репозиторий, ввести команду Git:
> git clone https://github.com/A-Sergey/Django-shop.git)

2. Создать виртуальное окружение.
###### *Windows:*
* в cmd.exe перейти в папку клонированного проекта
	> cd путь_проекта
* ввести команду:
	>python -m venv название_окружения
* для запуска виртуального окружения ввести команду: 
	>путь_проекта\название_окружения\Script\activate.bat
* установить необходимые библиотеки для проекта, ввести команду:
	>pip install -r requirements.txt
###### *Linux:*  
* в console перейти в папку клонированного проекта
  > cd путь_проекта
* ввести команду:
	> python3 -m venv название_окружения
* для запуска виртуального окружения ввести команду:
	> source путь_проект\название_окружения\bin\activate
* установить необходимые библиотеки для проекта, ввести команду:
	> pip install -r requirements.txt
3. Запустить миграцию командами
	#### *Windows:*
	> manage.py makemigrations accounts

	> manage.py makemigrations news

	> manage.py makemigrations products

	> manage.py migrate
	#### *Linux:*
	> python3 manage.py makemigrations accounts

	> python3 manage.py makemigrations news

	> python3 manage.py makemigrations products
	
	> python3 manage.py migrate
4. Запуск сервера командой
	#### *Windows:*
	> manage.py runserver
	#### *Linux:*
	> python3 manage.py runserver
5. Для тестового просмотра можно скачать готовую БД:
	> [готовая БД](https://drive.google.com/file/d/11mCdYFi2Fth4Rr70mVeiZkvEHkusWq0Z/view?usp=sharing "Готовая БД")
		 