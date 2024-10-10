from models import User
from schema import UserCreateSchema , UserDeleteSchema, UserGetSchema, UserUpdateSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session

def create_user_in_db(*, data: UserCreateSchema, db):
    new_user = User(username = data.username , password = data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg" : "new user is created"}


def delete_user_in_db(* , data: UserDeleteSchema, db):
    user = db.query(User).filter_by(username=data.username).first()
    if not user:
        raise HTTPException( status_code=404 , detail="user not found")
      
    db.delete(user)
    db.commit()
    return {"msg": "user is deleted"}


def get_user_by_username(*, username: str, db):
    user = db.query(User).filter_by(username=username).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    return UserGetSchema(username=user.username)





def update_user_in_db(user_name:str, new_username:str,   data: UserUpdateSchema, db: Session):
    user = db.query(User).filter_by(username=user_name , password=data.password).first()
 
    if not user :
        raise HTTPException(status_code=404, detail="password or username is incorrect")
    
    
    user.username = new_username  
    db.commit()
    db.refresh(user)

    return {"msg": "user is updated"}