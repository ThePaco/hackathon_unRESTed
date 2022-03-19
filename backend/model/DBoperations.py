import hashlib
import uuid
from sqlalchemy.orm import Session
import Models
from model.Schemas import CreateUser

#library of functions for creating, updating, searching and deleting db entries
def createUser(db: Session, user: CreateUser):
    passw_encoded = user.password.encode()
    password_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    public_id = str(uuid.uuid4())
    dbUser = Models.Person(publicId = public_id, firstName = user.firstName, lastName = user.lastName, isAdmin = False, role = user.role, teamId = user.teamId, email = user.email, password = password_sha256)
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

def createTeam(db: Session, team: Models.Team):
    public_id = str(uuid.uuid4())
    dbTeam = Models.Team(publicId = public_id, teamName = team.teamName)
    db.add(dbTeam)
    db.commit()
    return dbTeam

def updateTeam(db: Session, publicId: str):
    pass

def getAllTeams(db: Session):
    return db.query(Models.Team).all()

#evo ti tomislave snalazi se u ovome, i prije nego sto mi prigovaras podsjecam te da si ti ovako zelio
#ps. u slucaju da tereza/ana ovo cita, tomislav ti je ovo uvalio, ne ja :(
def getTeamByID(db: Session, teamPublicId: str):
    #get the team and all users in that team but it do be just concatenating json files
    team = db.query(Models.Team).filter(Models.Team.publicId == teamPublicId).first()
    usersInTeam = db.query(Models.Person).filter(Models.Person.teamId == teamPublicId).all()
    return team + usersInTeam

def deleteTeam(db: Session, publicId: str):
    dbUser = db.query(Models.Team).filter(Models.Team.publicId == publicId).first()
    db.delete(dbUser)
    db.commit()
    return(dbUser)

def createReservation(db: Session, reservation: Models.Reservation):
    public_id = str(uuid.uuid4())
    dbReservation = Models.Reservation(publicId = public_id, roomId = reservation.roomId, reservationStart = reservation.reservationStart, reservationEnd = reservation.reservationEnd)
    db.add(dbReservation)
    db.commit()
    return dbReservation

def getAllReservations(db: Session):
    return db.query(Models.Reservation).all()

def getReservationByID(db: Session, publicId: str):
    return db.query(Models.Reservation).filter(Models.Reservation.publicId == publicId).first()

def getReservationsForRoom(db:Session, roomId: str):
    return db.query(Models.Reservation).filter(Models.Reservation.roomId == roomId).all()

def deleteReservation(db: Session, publicId: str):
    pass

#HARDCODED TABLES - no create() or delete()
def updateRoom(db: Session, publicId: str, adminId: str, isAssigned: bool):
    dbRoom = db.query(Models.Room).filter(Models.Room.publicId == publicId).first()
    dbRoom.adminId = adminId
    dbRoom.isAssigned = isAssigned
    db.commit()
    return dbRoom

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

def getRoomsByFloor(db: Session, floorId: str):
    return db.query(Models.Room).filter(Models.Room.floorId == floorId).all()