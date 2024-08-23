from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from db.schemas import User as UserBase, UserResponse, UserUpdate
from db.session import get_db
from db.models import User

users = APIRouter()

@users.post('/')
async def create_user(data:UserBase, db:Session = Depends(get_db)):
    try:
        new_use = User(
            first_name = data.first_name,
            last_name = data.last_name,
            email = data.email
        )

        db.add(new_use)
        db.commit()

        return {'Status':'Successful'}
    
    except SQLAlchemyError as e:
        raise e
    except Exception as e:
        raise e

@users.get("/", response_model=List[UserResponse])
async def get_users(db:Session = Depends(get_db)):

    try:

        get_users: User = db.query(User).all()
        if not get_users:
            raise HTTPException(status_code=404, detail='Users not Found')

        return get_users
    
    except SQLAlchemyError as e:
        raise e
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e
    
@users.put('/{id}')
async def update_use(
    id:int = Path(...,),
    data: UserUpdate = Body(),
    db:Session = Depends(get_db)
):
    try:

        get_user: User = db.query(User).get(id)
        if not get_user:
            raise HTTPException(status_code=404, detail='User not Found')
        
        if data.first_name:
            get_user.first_name = data.first_name
        if data.last_name:
            get_user.last_name = data.last_name
        if data.email:
            get_user.email = data.email

        db.commit()

        return {'Status':'Successful'}

    except SQLAlchemyError as e:
        raise e
    except HTTPException as e:
        raise e
    except Exception as e:
        raise e

@users.delete('/{id}')
def delete_user(id:int = Path(...,), db:Session = Depends(get_db)):
    try:
        get_user: User = db.query(User).get(id)
        if not get_user:
            raise HTTPException(status_code=404, detail='User not Found')

        db.delete(get_user)
        db.commit()

        return {'Status':'Successful'}

    except SQLAlchemyError as e:
        raise e
    except HTTPException as e:
        raise e      
    except Exception as e:
        raise e