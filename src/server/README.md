# Server README

## To run background server

First ensure you have 2 seperate terminals; one dedicated for the client and one the server.

### Prerequisies to running server for development


> export FLASK_APP=mgflask

> export FLASK_ENV=development

### Running the server in development mode

1. Within the folder
> middleground/src/server/mgflask

2. Run the command 

> flask run

### Register new modulle
 
 1. Within the 
 > __init__.py 
  in the def create_app() import the module and call app.register_blueprint
  For example, if you have a folder foo/ with bar.py
  
  __init__.py 
  > from .foo import bar
  > 
  > def create_app():
  > 
  > ...
  > 
  > app.regiser_blueprint(foo.bp)
  > 
  > ...
  
  2) In foo/bar.py add this line 


  foo/bar.py
  > bp = Blueprint('bar', __name__)
  
 
 ### Database
 
 1) To init or reset the database call within middleground/src/server/mgflask
 
 > flask init-db
 
