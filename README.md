1.CREATE ENV
python -m venv venv
source venv/bin/activate
pip install django djangorestframework


2.RUN MIGRATION
python manage.py makemigrations
python manage.py migrate


3. RUN SERVER
 python manage.py runserver

4.API Endpoints

1. POST
  URL --- http://localhost:8000/api/users

{
    "id": 1,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 70
  }


  2. GET
    http://localhost:8000/api/users/1

 3.PUT
  http://localhost:8000/api/users/1

  {
    "id": 1,
    "first_name": "James",
    "last_name": "Butt",
    "company_name": "Benton, John B Jr",
    "city": "New Orleans",
    "state": "LA",
    "zip": 70116,
    "email": "jbutt@gmail.com",
    "web": "http://www.bentonjohnbjr.com",
    "age": 75
}

4.DELETE
http://localhost:8000/api/users/1





   


