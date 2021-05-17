from flask import Flask
from flask.cli import with_appcontext
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event

import click

#engine = create_engine('sqlite:///mgflask.db', convert_unicode=True)
engine = create_engine('sqlite:////tmp/mgflask.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


# enables foreign key constraints for SQLite
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('pragma foreign_keys=ON')


event.listen(engine, 'connect', _fk_pragma_on_connect)

Base = declarative_base()
Base.query = db_session.query_property()

def reset_db():
    Base.metadata.drop_all(bind=engine)

@click.command('reset-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    reset_db()
    click.echo('Initialized the database.')


def init_db():
    import mgflask.models
    Base.metadata.create_all(bind=engine)
    print('Created the database structure')


