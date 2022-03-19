from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model.Schemas import CreateReservation
from model import DBoperations
from model.Database import SessionLocal,engine
from fastapi.responses import JSONResponse
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

@router.post("/{room_id}")
async def createReservation(room_id, reservation : CreateReservation, db : Session = Depends(get_db)):
    reservations = DBoperations.getReservationsForRoom(db = db, roomId=room_id)
    for x in reservations:
        if (x.reservationStart < reservation.reservationStart) and (x.reservationEnd > reservation.reservationStart):
            return JSONResponse(status_code=400, content={"message": "Already Reserved"})
        if (x.reservationStart < reservation.reservationEnd) and (x.reservationEnd > reservation.reservationEnd):
            return JSONResponse(status_code=400, content={"message": "Already Reserved"})
    addedReservation = DBoperations.createReservation(reservation=reservation, db = db)
    return addedReservation

@router.get("/room/{public_id}")
async def getReservationsForRoom(public_id, db : Session = Depends(get_db)):
    reservations = DBoperations.getReservationsForRoom(db = db, roomId=public_id)
    return reservations 