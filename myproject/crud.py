from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()




def create_user(db: session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "Fake"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user





def get_items(db: session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_item(db: session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item