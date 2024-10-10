from fastapi import FastAPI, Depends
from db import get_db
from sqlalchemy.orm import session
from schema import UserCreateSchema , UserDeleteSchema, UserGetSchema, UserUpdateSchema
from service import create_user_in_db , delete_user_in_db, get_user_by_username, update_user_in_db
app = FastAPI()


@app.get("/")
def health_check():
    return { "msg": "health check is passed"}


@app.post("/user")
def create_user(item: UserCreateSchema, db: session = Depends(get_db)):
    message = create_user_in_db(data = item , db = db)
    return message


@app.delete("/user")
def delete_user(item: UserDeleteSchema, db: session = Depends(get_db)):
    message = delete_user_in_db(data=item, db=db)
    return message

@app.get("/user")
def get_user(username: str, db: session = Depends(get_db)):
    user = get_user_by_username(username=username, db=db)
    return user

                
@app.put("/user")
def update_user(username :str , new_username: str, item: UserUpdateSchema,  db: session = Depends(get_db)):
    message = update_user_in_db(user_name=username,new_username=new_username,data=item,db=db)
    return message