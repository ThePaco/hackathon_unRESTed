from venv import create
from fastapi import FastAPI, Depends, HTTPException
from backend.model import Models
from backend.model.DBoperations import createUser
from backend.model.Schemas import Login
from router import LoginRouter, PersonRouter, TeamRouter, FloorRouter, RoomRouter, ReservationRouter
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from model.Auth import AuthHandler

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/unprotected')
def unprotected():
    return { 'message': 'Hello World from unsecure' }

@app.post('/register', status_code=201)
def register(db: Session, login_details: Login):
    if db.query(Models.Person).filter(Models.Person.email == login_details.email).first():
        raise HTTPException(status_code=400, detail='Email is taken')
    login_details.password = login_details.get_password_hash(login_details.password)
    createUser(login_details)
    return


@app.post('/login')
def login(db: Session, login_details: Login):
    user = db.query(Models.Person).filter(Models.Person.email == login_details.email).first()
    
    if (user is None) or (not AuthHandler.verify_password(login_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid email and/or password')

    token = AuthHandler.encode_token(user['email'])
    return { 'token': token }


@app.get('/protected')
def protected(email=Depends(AuthHandler.auth_wrapper)):
    return { 'Email': email }


#app.include_router(LoginRouter.router, prefix("/login"), tags = ["login"])


app.include_router(LoginRouter.router, prefix="/login", tags=["login"])
app.include_router(PersonRouter.router, prefix="/person", tags=["person"])
app.include_router(FloorRouter.router, prefix="/floor", tags=["floor"])
app.include_router(RoomRouter.router, prefix="/room", tags=["room"])
app.include_router(TeamRouter.router, prefix="/team", tags=["team"])
app.include_router(ReservationRouter.router, prefix="/reservation", tags=["reservation"])
