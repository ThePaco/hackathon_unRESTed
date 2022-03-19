from sqlalchemy.orm import Session
from model import Models

def login(db: Session, email: str, password: str):
    person = db.query(Models.Person).filter(Models.Person.email == email, Models.Person.password== password).first()
    return person