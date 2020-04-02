# Quidco Coding Test

## Set Up

### Create a virtual enviroment for python3 

    Using Virtualenv

    virtualenv venv -p python3

### install requirements.txt

    pip install -r requirements.txt

### create a super user

    python manage.py createsuperuser

### make migrations for the admin interface

    python manage.py migrate

### run the server 

    python manage.py runserver

### log in into admin and create an api key

    localhost:8000/admin


### Add environment variables

    Change the .env file to match your api key created.
    Note these values would not be added to git but have been to ease set up
    
    
## Visit link for information on creating and using the api keys in requests

    https://florimondmanca.github.io/djangorestframework-api-key/guide/#creating-and-managing-api-keys
     
## Usage

### Search

    Make a GET requst to the following endpoint: localhost:8000/api/v1/gifs/search?title=Banana
    
    Where Banana can be any gif avaiable from the server.
    Searches are case-sensitive
    
### Random 

    Make a GET requst to the following endpoint: localhost:8000/api/v1/gifs/random
    
### Data Available in Test

    Currently the only availible titles can be searched:
    [
        {
            "title": "Banana",
            "url": "https://www.gifapi.com/banana.gif"
        },
        {
            "title": "Apple",
            "url": "https://www.gifapi.com/apple.gif"
        },
        {
            "title": "Pear",
            "url": "https://www.gifapi.com/pear.gif"
        },
        {
            "title": "Orange",
            "url": "https://www.gifapi.com/orange.gif"
        },
    ]
