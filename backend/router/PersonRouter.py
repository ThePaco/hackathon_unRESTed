from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateUser, PatchUser
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


@router.get("/")
async def getAllUsers(db : Session = Depends(get_db)):
    people = DBoperations.getAllUsers(db = db)
    return people


@router.get("/{public_id}")
async def getUserById (public_id, db : Session = Depends(get_db)):
    user = DBoperations.getUserByID(db = db, publicId=public_id)
    return {"publicId":public_id, "response": "GET person"}


@router.post("/")
async def createUser (user : CreateUser, db : Session = Depends(get_db)):
    addedUser = DBoperations.createUser(user = user, db = db)
    return {"publicId": addedUser.publicId, "response":"Added user"}

@router.patch("/{public_id}")
async def patchUser (user : PatchUser, public_id, db : Session = Depends(get_db)):
    user = DBoperations.updateUserTeam(db = db, user = user, publicId = public_id)
    return {"response": "User updated"}

@router.delete("/{public_id}")
async def deleteUser(public_id, db : Session = Depends(get_db)):
    DBoperations.deleteUser(db = db, publicId=public_id)
    return {"response": "User deleted"}