# Server README

## To run background server

1. First ensure you have 2 seperate terminals; one dedicated for the client and one the server.
2. Set up flask enviornment with the following commands

>   export FLASK_APP=webapp

>   export FLASK_ENV=development


 3. Within the folder basicneeds/server/src/webappRun the command
 
>    flask run

## Register new module

 1.   Within the init.py in the def create_app() import the module and call app.register_blueprint. 
For example, if you have a folder foo/ with bar.py

```
project
│   README.md
│   file001.txt    
│
└───webapp
│   │   __init__.py
|   |   auth.py
│   │   db.py
|   |   schema.sql
|   |   ...
│   │
│   └───foo
│       │   bar.py
│   
```

\_\_init_\_.py
```
from .foo import bar

def create_app():
 
    ... 
    app.register_blueprint(foo.bp)
    ...
```
 2.   In foo/bar.py add this line

foo/bar.py

```
...
bp = Blueprint('bar', __name__)
...
```

## Database

To init or reset the database call within basicneeds/server/src/webapp

 >  flask init-db


 
