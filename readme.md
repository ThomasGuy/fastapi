# Fastapi

An api in python mimicing an Instagram clone

use with <https://github.com/ThomasGuy/react-ui.git>

### add a .env file

for the 'SECRET_KEY' and 'DB_CONNECTION'

DB_CONNECTION = postgresql+psycopg2://user:passwrod\@localhost:5432/instagramdb

generate a unique id in a terminal type :- openssl rand -hex 32

### Create a local virtual enviroment

python3 -m venv .venv

source .venv/bin/activate

### install requirements

pip install -r requirements.txt

### start

uvicorn main:app --reload

go to 127.0.0.1:8000/docs
