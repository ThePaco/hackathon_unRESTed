from sqlite3 import Time
from xmlrpc.client import Boolean
from pydantic import BaseModel


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
    teamId: str

class CreateTeam(BaseModel):
    teamName: str

class PatchTeam(BaseModel):
    teamName: str

class PatchRoom(BaseModel):
    adminId: str
    isAssigned: bool

class CreateReservation(BaseModel):
    roomId: str
    reservationStart: Time
    reservationEnd: Time


