from telnetlib import SE
from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateTeam, PatchTeam
from model.Database import SessionLocal, engine
from sqlalchemy.orm import Session
from model import DBoperations

#Models.Base.metadata.create_all(bind=engine)  #UNCOMMENT TO REBUILD DATABASE


router = APIRouter() 

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def getAllTeams(db : Session = Depends(get_db)):
    teams = DBoperations.getAllTeams(db = db)
    return teams

@router.get("/{publicId}")
async def getTeam(publicId, db : Session = Depends(get_db)):
    team = DBoperations.getTeamByID(db = db, publicId = publicId)
    return team

@router.post("/")
async def createTeam(team : CreateTeam, db : Session = Depends(get_db)):
    addedTeam = DBoperations.createTeam(team = team, db = db)
    return {"publicId":addedTeam.publicId, "response": "Team added."}

@router.patch("/{publicId}")
async def updateTeam(team : CreateTeam, publicId, db : Session = Depends(get_db)):
    team = DBoperations.updateTeam(db = db, team =  team, publicId = publicId)
    return {"Response": "Team updated"}