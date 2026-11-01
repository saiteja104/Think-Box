from contextlib import asynccontextmanager

from fastapi import FastAPI

from common.db.database import Base, engine
from mgmt.models.user import User

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title = "ThinkBox API", lifespan=lifespan)

@app.get("/health")
def health_check():
    return {"status":"ok"}