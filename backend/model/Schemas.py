from datetime import date
from sqlite3 import Time
from xmlrpc.client import Boolean
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
    isAdmin: Boolean
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

class CreateReservation(BaseModel):
    roomId: str
    reservationStart: date
    reservationEnd: date

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
    workstationId: str

class PatchRoom(BaseModel):
    adminId: str
    isAssigned: bool

class CreateReservation(BaseModel):
    roomId: str
    reservationStart: Time
    reservationEnd: Time

