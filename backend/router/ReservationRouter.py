from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.model.Schemas import CreateReservation, PatchRoom
from model import Models
from model import DBoperations, Schemas
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
async def getAllReservations(db : Session = Depends(get_db)):
    reservations = DBoperations.getAllReservations(db = db)
    return reservations

@router.get("/{public_id}")
async def getReservation(public_id, db : Session = Depends(get_db)):
    reservation = DBoperations.getReservationByID(db = db, publicId=public_id)
    return reservation

@router.post("/")
async def createReservation(reservation = CreateReservation, db : Session = Depends(get_db)):
    addedReservation = DBoperations.createReservation(reservation=reservation, db = db)
    return addedReservation