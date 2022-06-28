
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


class Post(BaseModel):
    title: str
    content: str
    published: bool=True

class PostBase(Post):
    pass


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime


    class Config:
        orm_mode=True

class ResponsePost(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
        orm_mode=True


class PostOut(BaseModel):
    Post: ResponsePost
    likes: int

    class Config:
        orm_mode=True


class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]= None


class Vote(BaseModel):
    post_id:int
    dir: conint(le=1)