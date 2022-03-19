from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateUser, PatchUser
from model.Database import SessionLocal, engine
from sqlalchemy.orm import Session
from model import Crud

#Models.Base.metadata.create_all(bind=engine) #UNCOMMENT FROM DATABASE REBUILD
router = APIRouter()


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{public_id}")
async def getUserById (public_id, db : Session = Depends(get_db)):
    user = Crud.getUserByID(db = db, publicId=public_id)
    return {"publicId":public_id, "response": "GET person"}


@router.post("/")
async def createUser (user : CreateUser, db : Session = Depends(get_db)):
    addedUser = Crud.createUser(user = user, db = db)
    return {"publicId": addedUser.publicId, "response":"Added user"}

@router.patch("/{public_id}")
async def patchUser (user : CreateUser, public_id, db : Session = Depends(get_db)):
    user = Crud.updateUser(db = db, user = createUser, publicId = public_id)
    return {"response": "User updated"}