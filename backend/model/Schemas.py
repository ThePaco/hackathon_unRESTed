from datetime import date
from math import floor
from xmlrpc.client import Boolean
from pydantic import BaseModel

from backend.model.Models import Reservation, Workstation


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

class UpdateUserTeam(BaseModel):
    userPublicId: str
    teamPublicId: str

class GetUserById(BaseModel):
    publicId: str

class CreateTeam(BaseModel):
    teamName: str

class CreateReservation(BaseModel):
    publcId: str
    roomId: str
    reservationStart: date
    reservationEnd: date

class CreateRoom(BaseModel):
    adminId: str
    floorId: str
    isAssigned: bool

class CreateWorkstation(BaseModel):
    publicId: str
    workstationName: str
    roomId: str

class CreateFloor(BaseModel):
    publicId: str
    floorNumber: int

class CreateEquipment(BaseModel):
    publicId: str
    workstationId: str
