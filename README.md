# Card Scanner

For the project installation first you have to install docker using the link below 
https://docs.docker.com/engine/install/ubuntu/

Then you can run the Dockerfile from the project to setup the enviroment

On Windows
https://docs.docker.com/docker-for-windows/

On Linux
https://docs.docker.com/engine/reference/commandline/run/


To submit the image scanning requests make a post request into 
/scanner/new

To list all the cards on the system 
/scanner

the images will be processed using pytesseract to extract the data from them then the data will be stored into a database table which will be used to fetch the list of the cards on the website

Project Structure

.
├── card_scanner

│   ├── asgi.py

│   ├── __init__.py

│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── docker-compose.yml
├── Dockerfile
├── DockerImageContent
├── LICENSE
├── manage.py
├── README.md
├── requirements.tx
├── requirements.tx.save
└── scanner
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   ├── 0001_initial.py
    │   ├── 0002_card_source_image.py
    │   ├── 0003_card_create_date.py
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── scanner
    │       └── index.html
    ├── tests.py
    ├── urls.py
    └── views.py

