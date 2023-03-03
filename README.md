# wildberries_parsing
app for parsing wildberries items

## Setup

To run application adhere the following steps:
- clone this repository to your local machine
- intall docker in your system
- activate virtual environment with pipenv manager by commands: pipenv update, pipenv shell
- create .env file and set there environment variables: SECRET_KEY and DEBUG
- run the command: "docker build -t <image_name> ." (ignore quotes)
- run container with command: "docker run <image_name>" (ignore quotes)
- open in your browser http://0.0.0.0:8000/api/v1/goods 

step 2 can be missed if run application without containerization just with a command in terminal of porject: python manage.py runserver 

### Author

Roslik Dmitry
