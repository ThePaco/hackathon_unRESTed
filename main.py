from fastapi import FastAPI
from backend.router import LoginRouter, PersonRouter, TeamRouter
#from router import LoginRouter


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#app.include_router(LoginRouter.router, prefix("/login"), tags = ["login"])



app.include_router(LoginRouter.router, prefix="/login", tags=["login"])
app.include_router(PersonRouter.router, prefix="/person", tags=["person"])
