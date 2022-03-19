from sqlalchemy.orm import Session
import Models

def login(db: Session, email: str, password: str):
    db.query(Models.User).filter(Models.User.email == email, Models.User.password== password).first()