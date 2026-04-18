# Fastapi

An api in python mimicing an Instagram clone

use with <https://github.com/ThomasGuy/react-ui.git>

#### add a .env file

for the 'SECRET_KEY' and 'DB_CONNECTION'

DB_CONNECTION = postgresql+psycopg2://user:password\@localhost:5432/db

generate a unique id in a terminal type :- openssl rand -hex 32

#### Create a local virtual enviroment

python3 -m venv .venv . Activate it :- source .venv/bin/activate

install requirements:- pip install -r requirements.txt

### start

for debug /testing uvicorn main:app --reload . Then go to 127.0.0.1:8000/docs

else uvicorn main:app

#### recent update 04/2026::

Using UUID from native postgreSQL is faster for user id and public_id. This is not a native python type,

so we use "id: Mapped\[uuid.UUID\]" in the user model, to have a "uuid.UUID" type which pydantic can use.
