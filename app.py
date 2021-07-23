from fastapi import FastAPI
from api import router


app = FastAPI(
    title='Emphasoft Api',
    description='API by Aexandra Vorobeva'
)
app.include_router(router)