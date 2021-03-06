from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Time
from sqlalchemy.orm import relationship
import datetime
#from sqlite3 import Time


from .Database import Base

class Person(Base):
    __tablename__ = "Person"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    firstName = Column(String(40), nullable = False)
    lastName = Column(String(40), nullable = False)
    isAdmin = Column(Boolean, nullable = False)
    role = Column(String(40), nullable = False)
    teamId = Column(String(50), nullable = True)
    email = Column(String(50), nullable = False)
    password = Column(String(100), nullable = False)


class Team(Base):
    __tablename__ = "Team"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    teamName = Column(String(40), nullable = False)
    

class Workstation(Base):
    __tablename__ = "Workstation"

    id = Column(Integer, primary_key = True)
    workstationName = Column(String(40), nullable = False)
    publicID = Column(String(50), unique = True)
    roomId = Column(String(50), nullable = False)

class Room(Base):
    __tablename__ = "Room"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    adminId = Column(String(50), nullable = False)
    floorId = Column(String(50), nullable = False)
    isAssigned = Column(Boolean, nullable = False)
    
    
class Reservation(Base):
    __tablename__ = "Reservation"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    roomId = Column(String(50), nullable = False)
    reservationStart = Column(DateTime, nullable = False)
    reservationEnd = Column(DateTime, nullable = False)

class Floor(Base):
    __tablename__ = "Floor"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    floorNumber = Column(Integer, nullable = False)
    

class Equipment(Base):
    __tablename__ = "Equipment"

    id = Column(Integer, primary_key = True)
    publicId = Column(String(50), unique = True)
    equipmentName = Column(String(40), nullable = False)
    workstationId = Column(String(50), nullable = False)
