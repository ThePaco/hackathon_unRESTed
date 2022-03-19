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

class UpdateTeam(BaseModel):
    userPublicId: str
    teamPublicId: str

class PatchUser(BaseModel):
    teamId: str

class CreateTeam(BaseModel):
    teamName: str

class PatchTeam(BaseModel):
    teamName: str


