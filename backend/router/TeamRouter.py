from fastapi import APIRouter, Depends
from model import Models
from model.Schemas import CreateTeam, PatchTeam
from model.Database import SessionLocal, engine
from sqlalchemy.orm import Session
from model import Crud

#Models.Base.metadata.create_all(bind=engine)  #UNCOMMENT TO REBUILD DATABASE


router = APIRouter() 

#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def createTeam(team : CreateTeam, db : Session = Depends(get_db)):
    addedTeam = Crud.createTeam(team = team, db = db)
    return {"publicId":addedTeam.publicId, "response": "Team added."}

@router.patch("/{public_id}")
async def patchTeam(team : CreateTeam, public_id, db : Session = Depends(get_db)):
    team = Crud.updateTeam(db = db, team =  team, publicId = public_id)
    return {"Response": "Team updated"}