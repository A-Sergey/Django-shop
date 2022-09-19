FROM python:3.9

WORKDIR /usr/src/app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install psycopg2-binary
RUN python manage.py collectstatic --no-input

EXPOSE 1337