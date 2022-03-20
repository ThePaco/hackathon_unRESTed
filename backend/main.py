import hashlib
from typing_extensions import Self
from venv import create
from fastapi import FastAPI, Depends, HTTPException
from model import Models
from model.DBoperations import createUser
from model.Schemas import CreateUser, Login
from router import PersonRouter, TeamRouter, FloorRouter, RoomRouter, ReservationRouter, LoginRouter
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model.Auth import AuthHandler
from model.Database import SessionLocal, engine

app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

""" def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/unprotected')
def unprotected():
    return { 'message': 'Hello World from unsecure' }

@app.post('/register', status_code=201)
async def register(registration_details: CreateUser, db: Session = Depends(get_db)):
    if db.query(Models.Person).filter(Models.Person.email == registration_details.email).first():
        raise HTTPException(status_code=400, detail='Email is taken')
    passw_encoded = registration_details.password.encode()
    passw_encoded_sha256 = hashlib.sha256(passw_encoded).hexdigest()
    registration_details.password = passw_encoded_sha256
    createUser(db = db, user = registration_details)
    return registration_details


@app.post('/login')
async def login(raw_login_details):
    print("AAAAA")
    login_email = raw_login_details["email"]
    login_password = raw_login_details["password"]
    user = db.query(Models.Person).filter(Models.Person.email == login_email).first()

    if (user is None) or (not AuthHandler.verify_password(login_password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid email and/or password')

    token = AuthHandler.encode_token(user['email'])
    return { 'token': token }


@app.get('/protected')
def protected(email=Depends(AuthHandler.auth_wrapper)):
    return { 'Email': email } """


#app.include_router(LoginRouter.router, prefix("/login"), tags = ["login"])


app.include_router(LoginRouter.router, prefix="/login", tags=["login"])
app.include_router(PersonRouter.router, prefix="/person", tags=["person"])
app.include_router(FloorRouter.router, prefix="/floor", tags=["floor"])
app.include_router(RoomRouter.router, prefix="/room", tags=["room"])
app.include_router(TeamRouter.router, prefix="/team", tags=["team"])
app.include_router(ReservationRouter.router, prefix="/reservation", tags=["reservation"])
