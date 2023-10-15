## auction_system
### How to run 
cd into the auction system directory

    cd auction_system
create a virtul envirionment

    python3 -m venv

activate the venv

    source venv/bin/activate

install dependencies

    pip3 install -r requirements.txt

make migrations

    pyhthon manage.py makemigrations

create  a superuser

    python manage.py creatersuperuser

run the code

    python manage.py runserver
  
    

###NOTE 
Remember to set these values as envirionment variables on your machine

  - SECRET_KEY 
  - EMAIL_HOST_USER 
  - EMAIL_HOST_PASSWORD 
