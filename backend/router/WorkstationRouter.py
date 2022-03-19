from operator import ge
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.Schemas import CreateWorkstation
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
async def getAllWorkstations(db : Session = Depends(get_db)):
    workstations = DBoperations.getAllWorkstations(db = db)
    return workstations

@router.get("/{publicId}")
async def getWorkstationByID(publicId, db : Session = Depends(get_db)):
    workstation = DBoperations.getWorkstationByID(db = db, publicId=publicId)
    return workstation

@router.post("/")
async def createWorkstation(workstation = CreateWorkstation, db : Session = Depends(get_db)):
    addedWorkstation = DBoperations.createWorkstation(db = db, workstation=workstation)
    return {"publicId":addedWorkstation.publicId, "response":"Workstation created"}


