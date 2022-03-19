from fastapi import FastAPI
from router import LoginRouter, PersonRouter, TeamRouter, FloorRouter, RoomRouter, ReservationRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_methods=[""],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}



#app.include_router(LoginRouter.router, prefix("/login"), tags = ["login"])



app.include_router(LoginRouter.router, prefix="/login", tags=["login"])
app.include_router(PersonRouter.router, prefix="/person", tags=["person"])
app.include_router(FloorRouter.router, prefix="/floor", tags=["floor"])
app.include_router(RoomRouter.router, prefix="/room", tags=["room"])
app.include_router(TeamRouter.router, prefix="/team", tags=["team"])
app.include_router(ReservationRouter.router, prefix="/reservation", tags=["reservation"])

