from fastapi import FastAPI
from database import engine
import models
from routers import heroes_router, auth_router, admin_router, players_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bienvenue dans l'API Dungeons & Dragons 🚀"}


models.Base.metadata.create_all(bind=engine)

app.include_router(heroes_router.router)
app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(players_router.router)
