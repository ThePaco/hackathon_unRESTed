from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.model.Schemas import CreateFloor
from model import DBoperations
from model.Database import SessionLocal
#Models.Base.metadata.create_all(bind=engine)  #UNCOMMENT TO REBUILD DATABASE


router = APIRouter() 

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{publicId}")
async def getFloorByID(publicId, db: Session = Depends(get_db)):
    floor = DBoperations.getFloorByID(db = db, publicId = publicId)
    return floor

@router.get("/{publicId}/rooms")
async def getRoomsOnFloor(publicId, db: Session = Depends(get_db)):
    floor = DBoperations.getRoomsOnFloor(publicId = publicId, db = db)
    return floor

@router.get("/")
async def getAllFloors(db: Session = Depends(get_db)):
    floor = DBoperations.getAllFloors(db = db)
    return floor

@router.post("/")
async def createFloor(floor : CreateFloor, db : Session = Depends(get_db)):
    floor = DBoperations.createFloor(db = db, floor = floor)
    return {"response": "floor created", "publicId": floor.publicId}