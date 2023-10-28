from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine

from fastapi import FastAPI

from .routes import users, wishlists, items

from app.models import user

user.Base.metadata.create_all(bind=engine)

app = FastAPI(title="wishlist", version="1.0.0")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(wishlists.router)
app.include_router(items.router)

@app.get("/healthchecker", tags=['Health check'])
def root():
    return {"app": f"{app.title}", "version": f"{app.version}"}