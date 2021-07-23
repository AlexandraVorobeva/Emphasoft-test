from fastapi import FastAPI
from api import router


app = FastAPI(
    title='Emphasoft Api'
)
app.include_router(router)