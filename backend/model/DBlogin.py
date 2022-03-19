from sqlalchemy.orm import Session
import Models
from DBlogin import login
from Schemas import Login

def login(db: Session, user: Login):
    return db.query(Models.Person).filter(Models.Person.email == user.email, Models.Person.password == user.password).first()