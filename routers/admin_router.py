from fastapi import HTTPException, APIRouter, Depends, Path
from starlette import status
from database import db_dependency
from models import Heroes
from routers.auth_router import player_dependency

router = APIRouter(
    tags=["admin"],
    prefix="/admin"
)

# GET ALL HEROES (AS ADMIN)
@router.get("/heroes", status_code=status.HTTP_200_OK)
async def get_all_heroes(player: player_dependency, db: db_dependency):
    if player is None or player.get("player_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Heroes).order_by(Heroes.id.asc()).all()
    # Return can be empty

# DELETE (BY ID AS PATH PARAM) (AS ADMIN)
@router.delete("/heroes/delete/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(player: player_dependency, db: db_dependency, hero_id: int = Path(gt=0)):
    if player is None or player.get("player_role") != "admin":
        raise HTTPException(status_code=401, detail="Authentication failed")
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).first()
    if hero_db is None:
        raise HTTPException(status_code=404, detail="Hero can't be found")
    db.delete(hero_db)
    db.commit()