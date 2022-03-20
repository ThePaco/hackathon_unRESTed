from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateUser, PatchUser, Login
from model.Database import SessionLocal, engine
from sqlalchemy.orm import Session
from model import DBoperations


#Models.Base.metadata.create_all(bind=engine) #UNCOMMENT FROM DATABASE REBUILD
router = APIRouter()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def login(user : CreateUser, db : Session = Depends(get_db)):
    user = DBoperations.userLogin(db = db, user = user)
    return user
