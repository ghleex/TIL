import urllib
import os
from databases.core import DatabaseURL

from sqlalchemy.sql import sqltypes

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'fastapi')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgresql')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'secret')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode', 'prefer')))
DATABASE_URL = f'postgresql://{db_username}:{db_password}@{host_server}:{db_server_port}/{database_name}?sslmode={ssl_mode}'


import sqlalchemy

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    'notes',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('text', sqlalchemy.String),
    sqlalchemy.Column('completed', sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    # DATABASE_URL, connect_args={'check_same_thread': False}
    DATABASE_URL, pool_size=3, max_overflow=0
)

metadata.create_all(engine)



from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title='REST API using FastAPI PostgreSQL Async EndPoints')
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


import databases

database = databases.Database(DATABASE_URL)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.post('/notes', response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, complete=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), 'id': last_record_id}
