from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.model.Models import Equipment
from backend.model.Schemas import CreateEquipment
from model.Schemas import CreateFloor
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

@router.get("/")
async def getAllEquipment(db : Session = Depends(get_db)):
    equipment = DBoperations.getAllEquipment(db = db)
    return equipment

@router.get("/{publicId}")
async def getEquipmentByID(publicId, db : Session = Depends(get_db)):
    equipment = DBoperations.getEquipmentByID(db = db, publicId=publicId)
    return equipment

@router.post("/")
async def createEquipment(equipment: CreateEquipment, db : Session = Depends(get_db)):
    addedEquipment = DBoperations.createEquipment(db = db, equipment=equipment)
    return {"response": "equipment created", "publicId": addedEquipment.publicId}