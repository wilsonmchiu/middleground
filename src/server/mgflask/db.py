from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event
import json

with open('creds.json') as data_file:
    data = json.load(data_file)

CLOUDSQL_USER = data['GCSQL']['username']
CLOUDSQL_PASSWORD = data['GCSQL']['password']
CLOUDSQL_DATABASE = data['GCSQL']['db-name']
CLOUDSQL_CONNECTION_NAME = data['GCSQL']['connection-name']

LOCAL_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
)

LIVE_SQLALCHEMY_DATABASE_URI = (
    'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
    nam=CLOUDSQL_USER,
    pas=CLOUDSQL_PASSWORD,
    dbn=CLOUDSQL_DATABASE,
    con=CLOUDSQL_CONNECTION_NAME,
)

# Use this for local deployment. make sure to use Google Cloud Proxy
engine = create_engine(LOCAL_SQLALCHEMY_DATABASE_URI, convert_unicode=True)

# Use this for deployments
# engine = create_engine(LIVE_SQLALCHEMY_DATABASE_URI, convert_unicode=True)

# Use this for local testing. make sure to uncomment lines below 
# engine = create_engine('sqlite:////tmp/mgflask.db', convert_unicode=True)
# # enables foreign key constraints for SQLite
# def _fk_pragma_on_connect(dbapi_con, con_record):
#     dbapi_con.execute('pragma foreign_keys=ON')
# event.listen(engine, 'connect', _fk_pragma_on_connect)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

# original sql_mode causes a lot of problems. TRADITIONAL seems to work
def connect(dbapi_con, connection_record):
        cur = dbapi_con.cursor()
        cur.execute("SET SESSION sql_mode='TRADITIONAL'")
        cur = None

event.listen(engine, 'connect', connect)


Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import mgflask.models
    Base.metadata.create_all(bind=engine)
    print('Created the database structure')



