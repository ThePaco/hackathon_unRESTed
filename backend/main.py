from fastapi import FastAPI
from router import LoginRouter, PersonRouter, TeamRouter
from fastapi.middleware.cors import CORSMiddleware

#from router import LoginRouter


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
