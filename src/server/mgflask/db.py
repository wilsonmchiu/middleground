from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event
import json
import os
import mgflask


def _fk_pragma_on_connect(dbapi_con, con_record):
    # enables foreign key constraints for SQLite
    dbapi_con.execute('pragma foreign_keys=ON')


parent_dir = os.path.dirname(os.path.dirname(mgflask.__file__)) #this makes sure creds.json can always be found
with open(parent_dir+'/creds.json') as data_file:  
    data = json.load(data_file)
CLOUDSQL_USER = data['GCSQL']['username']
CLOUDSQL_PASSWORD = data['GCSQL']['password']
CLOUDSQL_DATABASE = data['GCSQL']['db-name']
CLOUDSQL_CONNECTION_NAME = data['GCSQL']['connection-name']

LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format(
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format(
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)

print("FLASK_ENV=",os.environ.get('FLASK_ENV'))
if (os.environ.get('FLASK_ENV') is None):
    engine = create_engine('sqlite:///mgflask.db', convert_unicode=True)
    event.listen(engine, 'connect', _fk_pragma_on_connect)
elif (os.environ.get('FLASK_ENV') == "development"):
    # Use this for to access the Google Cloud SQL db. make sure to use Google Cloud Proxy
    engine = create_engine(LOCAL_SQLALCHEMY_DATABASE_URI, convert_unicode=True)
else:
    # Use this for deployments
    engine = create_engine(LIVE_SQLALCHEMY_DATABASE_URI, convert_unicode=True)


db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import mgflask.models
    Base.metadata.create_all(bind=engine)
    print('Created the database structure')
