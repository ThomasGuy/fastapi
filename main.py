from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from src.auth import authentication
from src.database import engine, models
from src.router import comment_api, post_api, user_api

app = FastAPI()

app.include_router(user_api.router)
app.include_router(post_api.router)
app.include_router(comment_api.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(bind=engine)

app.mount('/src/images', StaticFiles(directory='src/images'), name='images')

origins = ['http://127.0.0.1:5173', 'http://127.0.0.1:5174', 'http://127.0.0.1:4173']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
