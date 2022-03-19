from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateUser, PatchUser
from model.Database import SessionLocal, engine
from sqlalchemy.orm import Session
from model import DBoperations

Models.Base.metadata.create_all(bind=engine) #UNCOMMENT FROM DATABASE REBUILD
router = APIRouter()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def getAllUsers(db : Session = Depends(get_db)):
    people = DBoperations.getAllUsers(db = db)
    return people


@router.get("/{publicId}")
async def getUserById (publicId, db : Session = Depends(get_db)):
    user = DBoperations.getUserByID(db = db, publicId=publicId)
    return {"publicId":publicId, "response": "GET person"}


@router.post("/")
async def createUser (user : CreateUser, db : Session = Depends(get_db)):
    addedUser = DBoperations.createUser(user = user, db = db)
    return {"publicId": addedUser.publicId, "response":"Added user"}

@router.patch("/{publicId}")
async def updateUserTeam (user : PatchUser, publicId, db : Session = Depends(get_db)):
    user = DBoperations.updateUserTeam(db = db, user = user, publicId = publicId)
    return {"response": "User updated"}

@router.delete("/{publicId}")
async def deleteUser(publicId, db : Session = Depends(get_db)):
    DBoperations.deleteUser(db = db, publicId=publicId)
    return {"response": "User deleted"}