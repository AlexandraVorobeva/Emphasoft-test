from fastapi import FastAPI
import uvicorn
from api import router


app = FastAPI(title="Emphasoft Api", description="API by Aexandra Vorobeva")
app.include_router(router)


if __name__ == '__main__':

    uvicorn.run(app)