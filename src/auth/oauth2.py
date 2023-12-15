from datetime import datetime, timedelta
from typing import Annotated, Any, Union

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from mysqlx import Session
from pydantic import ValidationError
from .. import database




from ..config import settings
from ..utils.passwd_utils import pwd_context, get_password_hash, verify_password
from ..schemas import user
from ..schemas.token import TokenPayload
from ..models import user as user_model
# to get a string like this run:
# openssl rand -hex 32
JWT_SECRET_KEY = settings.jwt_secret_key #"09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
JWT_REFRESH_SECRET_KEY = settings.jwt_refresh_secret_key
ALGORITHM = settings.algorithm #"HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes #30
REFRESH_TOKEN_EXPIRE_MINUTES = settings.refresh_token_expire_minutes 

reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl="/login",
    scheme_name="JWT"
    #scopes={"me": "Read information about the current user.", "items": "Read items."},
)



def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
    """
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])

        token_data = TokenPayload(**payload)

        if datetime.fromtimestamp(token_data.exp) < datetime.now():
            raise HTTPException(
                status_code = status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )


    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return token_data


def get_current_user(token: str = Depends(reuseable_oauth), db: Session = Depends(database.get_db)) -> user.SystemUser:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    token_data = verify_access_token(token)

    usr = db.query(user_model.User).filter(user_model.User.id == token_data.sub).first()

    if usr is None:
        raise credentials_exception

    return user.SystemUser(id= usr.id, email= usr.email, password= usr.password)

