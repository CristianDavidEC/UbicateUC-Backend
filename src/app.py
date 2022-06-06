from this import s
from fastapi import FastAPI
from routes.SitiosRoutes import sitio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
  title="Backend UbicateUC, semillero de investigacion SOLID",
)

origins = [
    "http://localhost",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(sitio)