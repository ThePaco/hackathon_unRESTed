import datetime
import hashlib
import uuid
from sqlalchemy import true
from sqlalchemy.orm import Session
from model.Schemas import CreateUser
from model.Schemas import Login

from model import Models
from model import Schemas

#library of functions for creating, updating, searching and deleting db entries
def createUser(db: Session, user: Schemas.CreateUser):
    #passw_encoded = user.password.encode()
    #password_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    public_id = str(uuid.uuid4())
    dbUser = Models.Person(publicId = public_id, firstName = user.firstName, lastName = user.lastName, isAdmin = False, role = user.role, teamId = user.teamId, email = user.email, password = user.password)
    db.add(dbUser)
    db.commit()
    return dbUser

def updateUserTeam(db: Session, user: Schemas.UpdateUserTeam):
    dbUser = db.query(Models.Person).filter(Models.Person.publicId == user.userPublicId).first()
    dbUser.teamId = user.teamPublicId
    db.commit()
    return dbUser

def promoteUser(db: Session, userPublicId: str):
    dbUser = db.query(Models.Person).filter(Models.Person.publicId == userPublicId).first()
    dbUser.isAdmin = 1
    db.commit()
    return dbUser

def getAllUsers(db: Session):
    return db.query(Models.Person).all()

def getUserByID(db: Session, publicId: str):
    return db.query(Models.Person).filter(Models.Person.publicId == publicId).first()

def deleteUser(db: Session, user: Schemas.GetUserById):
    dbUser = db.query(Models.Person).filter(Models.Person.publicId == user.publicId).first()
    db.delete(dbUser)
    db.commit()
    return(dbUser)



def createTeam(db: Session, team: Schemas.CreateTeam):
    public_id = str(uuid.uuid4())
    dbTeam = Models.Team(publicId = public_id, teamName = team.teamName)
    db.add(dbTeam)
    db.commit()
    return dbTeam

#no clue what this should do
def updateTeam(db: Session, publicId: str):
    pass

def getAllTeams(db: Session):
    return db.query(Models.Team).all()

#evo ti tomislave snalazi se u ovome, i prije nego sto mi prigovaras podsjecam te da si ti ovako zelio
#ps. u slucaju da tereza/ana ovo cita, tomislav ti je ovo uvalio, ne ja :(
def getTeamByID(db: Session, teamPublicId: str):
    #get the team and all users in that team but it do be just concatenating json files
    team = db.query(Models.Team).filter(Models.Team.publicId == teamPublicId).first()
    users = db.query(Models.Person.publicId, Models.Person.firstName, Models.Person.lastName).filter(Models.Person.teamId == teamPublicId).all()
    return team + users

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
    dbReservation = db.query(Models.Reservation).filter(Models.Reservation.publicId == publicId).first()
    db.delete(dbReservation)
    db.commit()
    return(dbReservation)



def createRoom(db: Session, room: Schemas.CreateRoom):
    public_id = str(uuid.uuid4())
    dbRoom = Models.Room(publicId = public_id, adminId = room.adminId, floorId = room.floorId, isAssigned = room.isAssigned)
    db.add(dbRoom)
    db.commit()
    return dbRoom

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


def createWorkstation(db: Session, workstation: Schemas.CreateWorkstation):
    public_id = str(uuid.uuid4())
    dbWorkstation = Models.Room(publicId = public_id, workstationName = Schemas.CreateWorkstation.workstationName, roomId = Schemas.CreateWorkstation.roomId)
    db.add(dbWorkstation)
    db.commit()
    return dbWorkstation

def getAllWorkstations(db: Session):
    return db.query(Models.Workstation).all()

def getWorkstationByID(db: Session, publicId: str):
    return db.query(Models.Workstation).filter(Models.Workstation.publicId == publicId).first()



def createFloor(db: Session, floor: Schemas.CreateFloor):
    public_id = str(uuid.uuid4())
    dbFloor = Models.Floor(publicId = public_id, floorNumber = floor.floorNumber)
    db.add(dbFloor)
    db.commit()
    return dbFloor

def getAllFloors(db: Session):
    return db.query(Models.Floor).all()

def getFloorByID(db: Session, publicId: str):
    return db.query(Models.Floor).filter(Models.Floor.publicId == publicId).first()

def getRoomsByFloor(db: Session, floorId: str):
    return db.query(Models.Room).filter(Models.Room.floorId == floorId).all()

def createEquipment(db : Session, equipment = Schemas.CreateEquipment):
    public_id = str(uuid.uuid4())
    dbEquipment = Models.Equipment(publicId = public_id, equipment = equipment.equipmentName, workstationId = equipment.workstationId)
    db.add(dbEquipment)
    db.commit()
    return dbEquipment

def getAllEquipment(db : Session):
    return db.query(Models.Equipment).all()

def getEquipmentByID(db : Session, publicId: str):
    return db.query(Models.Equipment).filter(Models.Equipment.publicId == publicId).first()


def userLogin(db : Session, user : CreateUser):
    return db.query(Models.Person).filter(
      Models.Person.email == user.email,
      Models.Person.password == user.password
      ).first()
