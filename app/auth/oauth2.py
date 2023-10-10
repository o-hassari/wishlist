from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from mysqlx import Session
from app import database



from config import settings
from ..utils.passwd_utils import pwd_context, get_password_hash, verify_password
from ..schemas import token
from ..models import user
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = settings.secret_key #"09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = settings.algorithm #"HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes #30


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    #scopes={"me": "Read information about the current user.", "items": "Read items."},
)



def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = token.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(user.User.id).filter(user.User.id == token.id).first()

    return user

