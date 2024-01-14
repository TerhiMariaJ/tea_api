from sqlalchemy.orm import Session

from . import models, schemas


def get_tea(db: Session, tea_id: int):
    return db.query(models.Tea).filter(models.Tea.id == tea_id).first()


def get_tea_by_name(db: Session, name: str):
     return db.query(models.Tea).filter(models.Tea.name == name).first()

def get_tea_by_tea_name(db: Session, tea_name: str):
     return db.query(models.Tea).filter(models.Tea.name == tea_name).first()

def get_tea_by_type(db: Session, tea_type: str):
     return db.query(models.Tea).filter(models.Tea.type == tea_type).first()


def get_teas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tea).offset(skip).limit(limit).all()


def create_tea(db: Session, tea: schemas.TeaCreate):

    db_tea = models.Tea(name=tea.name, type=tea.type)
    db.add(db_tea)
    db.commit()
    db.refresh(db_tea)
    return db_tea

def delete_tea(db: Session, tea_id:int):
    db_tea = db.query(models.Tea).filter(models.Tea.id == tea_id).first()

    if db_tea:
        db.delete(db_tea)
        db.commit()

    return db_tea




