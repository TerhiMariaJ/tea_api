from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tea/", response_model=schemas.Tea)
def create_tea(tea: schemas.TeaCreate, db: Session = Depends(get_db)):
    db_tea = crud.get_tea_by_name(db, name=tea.name)
    if db_tea:
        raise HTTPException(status_code=400, detail="Tea already registered")
    return crud.create_tea(db=db, tea=tea)


@app.get("/tea/", response_model=list[schemas.Tea])
def get_teas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teas = crud.get_teas(db, skip=skip, limit=limit)
    return teas


@app.get("/tea/{tea_id}", response_model=schemas.Tea)
def get_tea(tea_id: int, db: Session = Depends(get_db)):
    db_tea = crud.get_tea(db, tea_id=tea_id)
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    return db_tea


@app.get("/tea/name/{tea_name}", response_model=schemas.Tea)
def get_tea_by_tea_name(tea_name: str, db: Session = Depends(get_db)):
  db_tea = crud.get_tea_by_tea_name(db, tea_name=tea_name)
  if db_tea is None:
         raise HTTPException(status_code=404, detail="Tea not found")
  return db_tea

@app.get("/tea/type/{tea_type}", response_model=schemas.Tea)
def get_tea_by_type(tea_type: str, db: Session = Depends(get_db)):
     db_tea = crud.get_tea_by_type(db, tea_type=tea_type)
     if db_tea is None:
         raise HTTPException(status_code=404, detail="Tea not found")
     return db_tea

@app.delete("/tea/{tea_id}", response_model=schemas.Tea)
def delete_tea(tea_id: int, db: Session = Depends(get_db)):
    db_tea = crud.get_tea(db, tea_id=tea_id)
    if db_tea is None:
        raise HTTPException(status_code=404, detail="Tea not found")
    return crud.delete_tea(db=db, tea_id=tea_id)
