import hashlib
import os
import uuid
from fastapi import UploadFile
from sqlalchemy.orm import Session
from backend.model.Models import Reservation, Team
from model import Models
from model.Schemas import CreateUser, PatchUserForm

def createUser(user: CreateUser, db: Session):
    passw_encoded = user.password.encode()
    password_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    public_id = str(uuid.uuid4())
    dbUser = Models.Person(publicId = public_id, firstName = user.firstName, lastName = user.lastName, isAdmin = False, role = user.role, teamID = user.teamId, email = user.email, password = password_sha256)
    db.add(dbUser)
    db.commit()
    return dbUser

def updateUserTeam(db: Session, userPublicID: str, teamPublicId : str):
    dbUser = db.query(Models.Person).filter(Models.Person.publicId == userPublicID).first()
    dbUser.teamID = teamPublicId
    db.commit()
    return dbUser

def getAllUsers(db: Session):
    return db.query(Models.Person).all()

def getUserByID(db: Session, publicId: str):
    return db.query(Models.Person).filter(Models.Person.publicId == publicId).first()

def deleteUser(db: Session, publicId: str):
    dbUser = db.query(Models.Person).filter(Models.Person.publicId == publicId).first()
    db.delete(dbUser)
    db.commit()
    return(dbUser)

def createTeam(team: Team, db:Session):
    public_id = str(uuid.uuid4())
    dbTeam = Models.Team(publicId = public_id, teamName = team.teamName)
    db.add(dbTeam)
    db.commit()
    return dbTeam

#not implemented/used
def updateTeam():
    pass

def getAllTeams(db: Session):
    return db.query(Models.Team).all()

def getTeamByID(db: Session, publicId: str):
    return db.query(Models.Team).filter(Models.Team.publicId == publicId).first()

def deleteTeam(db: Session, publicId: str):
    dbUser = db.query(Models.Team).filter(Models.Team.publicId == publicId).first()
    db.delete(dbUser)
    db.commit()
    return(dbUser)

def createReservation(reservation: Reservation, db: Session):
    public_id = str(uuid.uuid4())
    dbReservation = Models.Reservation(publicId = public_id, roomId = reservation.roomId, reservationStart = reservation.reservationStart, reservationEnd = reservation.reservationEnd)
    db.add(dbReservation)
    db.commit()
    return dbReservation

def getAllReservations(db: Session):
    return db.query(Models.Reservation).all()

def getReservationByID(db: Session, publicId: str):
    return db.query(Models.Reservation).filter(Models.Reservation.publicId == publicId).first()

def deleteReservation(db: Session, publicId: str):
    pass

#HARDCODED TABLES - no create() or delete()
def getAllRooms(db: Session):
    return db.query(Models.Room).all()

def getRoomByID(db: Session, publicId: str):
    return db.query(Models.Room).filter(Models.Room.publicId == publicId).first()

def getAllWorkstations(db: Session):
    return db.query(Models.Workstation).all()

def getWorkstationByID(db: Session, publicId: str):
    return db.query(Models.Workstation).filter(Models.Workstation.publicId == publicId).first()

def getAllFloors(db: Session):
    return db.query(Models.Floor).all()

def getFloorByID(db: Session, publicId: str):
    return db.query(Models.Floor).filter(Models.Floor.publicId == publicId).first()
