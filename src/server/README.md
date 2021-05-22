# Server README

## To run background server

1. First ensure you have 2 seperate terminals; one dedicated for the client and one the server.
2. Navigate to the server folder

    ```sh
    $ cd middleground/src/server
    ```

3. Create and activate Python Virtual Environment

    ```sh
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    ```
    

4. Set up the Flask app

    ```sh
    (env)$ export FLASK_APP=mgflask
    ```
    
    Windows: 
    ```
    (env)C:\ ... \MiddleGround\middleground\src\server\mgflask > set FLASK_APP=mgflask
    ```
    
5. If you want to locally access the remote database (start up Cloud SQL Auth proxy as well)

    ```sh
    (env)$ export FLASK_ENV=development
    ```
    
    Windows: 
    ```sh
    (env)C:\ ... \MiddleGround\middleground\src\server\mgflask > set FLASK_ENV=development
    ```
    
    Get the middleground.json credentials from project owner and run this command:
    ```sh
    ./cloud_sql_proxy -instances=middleground-314106:us-central1:final-instance-id=tcp:3306 -credential_file=middleground-314106-b99091a90bd9.json
    ```

6. If you want to locally access the local database (SQLite):
    Don't export anything for FLASK_ENV
    
7. If you're deploying to the remote database:
    ```sh
    (env)$ export FLASK_ENV=production
    ```
    Windows: 
    ```
    (env)C:\ ... \MiddleGround\middleground\src\server\mgflask > set FLASK_ENV=production
    ```
8. Run the app
    ```sh
    (env)$ flask run
    ```
    Windows: 
    ```
    (env)C:\ ... \MiddleGround\middleground\src\server\mgflask > flask run
    ```
    
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


 
