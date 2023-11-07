from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas.user import UserOut

from src.schemas.user import SystemUser, UserAuth

from .database import engine

from fastapi import FastAPI

from .routes import users, wishlists, items, auth


from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .auth.oauth2 import create_access_token, create_refresh_token, get_current_user
from .database import get_db

from .schemas.token import TokenSchema
from .utils.passwd_utils import verify_password

from .models import user as user_model
#user.Base.metadata.create_all(bind=engine)

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

@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.email == form_data.username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )
    
    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }

@app.get('/me', summary='Get details of currently logged in user', response_model=UserOut) # UserAuth
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user