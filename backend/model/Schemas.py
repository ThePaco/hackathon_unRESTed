from datetime import datetime
from sqlite3 import Time
from pydantic import BaseModel


from model.Models import Reservation, Workstation

class Login(BaseModel):
    email: str
    password: str

class CreateUser(BaseModel):
    firstName: str
    lastName: str
    role: str
    teamId: str
    email: str
    password: str

class PatchUser(BaseModel):
    firstName: str
    lastName: str
    isAdmin: bool
    role: str
    teamId: str
    email: str
    password: str

class PatchTeam(BaseModel):
    teamName: str

class UpdateUserTeam(BaseModel):
    userPublicId: str
    teamPublicId: str

class GetUserById(BaseModel):
    publicId: str

class CreateTeam(BaseModel):
    teamName: str


class CreateRoom(BaseModel):
    adminId: str
    floorId: str
    isAssigned: bool

class CreateWorkstation(BaseModel):
    workstationName: str
    roomId: str

class CreateFloor(BaseModel):
    floorNumber: int

class CreateEquipment(BaseModel):
    equipmentName: str
    workstationId: str
    

class PatchRoom(BaseModel):
    adminId: str
    isAssigned: bool

class CreateReservation(BaseModel):
    roomId: str
    reservationStart: datetime
    reservationEnd: datetime

