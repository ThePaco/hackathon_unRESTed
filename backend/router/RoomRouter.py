from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.model.Schemas import PatchRoom
from model import Models
from model import DBoperations
from model.Database import SessionLocal,engine
#Models.Base.metadata.create_all(bind=engine)  #UNCOMMENT TO REBUILD DATABASE

router = APIRouter() 

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def getAllRooms(db : Session):
    rooms = DBoperations.getAllRooms(db = db)
    return rooms

@router.get("/{publicId}")
async def getRoom(publicId, db: Session = Depends(get_db)):
    room = DBoperations.getRoom(publicId = publicId, db = db)
    return room


@router.patch("/{publicId}")
async def updateRoom(publicId, patch : PatchRoom, db: Session = Depends(get_db)):
    room = DBoperations.updateRoom(publicId = publicId, adminId = patch.adminId, isAssigned = patch.isAssigned, db = db)
    return {"response": "Room patched"}