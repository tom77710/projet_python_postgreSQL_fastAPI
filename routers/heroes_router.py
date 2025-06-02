from fastapi import Query, Path, Body, HTTPException, APIRouter, Depends
from classes import HeroValidation
from starlette import status
from database import db_dependency, engine
from sqlalchemy import text
import models
from models import Heroes
from routers.auth_router import player_dependency

router = APIRouter(
    tags=["heroes"],
    prefix="/heroes"
)

@router.get("/heartbeat")
async def heartbeat(db: db_dependency):
    try:
        db.execute(text("SELECT 1"))
        return { "message": "DATABASE OK" }
    except Exception as e:
        return { "error": str(e) }

# GET ALL (FOR THE LOGGED PLAYER)
@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_heroes(player: player_dependency, db: db_dependency):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Heroes).filter(Heroes.owner_id == player.get("id")).order_by(Heroes.id.asc()).all()
    # Return can be empty

# GET BY TYPE (AS QUERY PARAM) (FOR THE LOGGED PLAYER)
@router.get("/type", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_type(player: player_dependency, db: db_dependency, hero_type: str = Query()):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    result = db.query(Heroes).filter(Heroes.type.ilike(f"%{hero_type}%")).filter(Heroes.owner_id == player.get("id")).all()
    return result
    # Return can be empty

# GET BY RANK (AS QUERY PARAM) (FOR THE LOGGED PLAYER)
@router.get("/rank", status_code=status.HTTP_200_OK)
async def get_all_heroes_by_rank(player: player_dependency, db: db_dependency, hero_rank: int = Query(ge=0, le=100)):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    result = db.query(Heroes).filter(Heroes.rank >= hero_rank).filter(Heroes.owner_id == player.get("id")).all()
    return result
    # Return can be empty

# GET ONE HERO BY ID (AS PATH PARAM) (FOR THE LOGGED PLAYER)
@router.get("/id/{hero_id}", status_code=status.HTTP_200_OK)
async def get_one_hero_by_id(player: player_dependency, db: db_dependency, hero_id: int = Path(gt=0)):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).filter(Heroes.owner_id == player.get("id")).first()
    if hero_db is not None:
        return hero_db
    raise HTTPException(status_code=404, detail="Hero can't be found")

# GET ONE HERO BY NICKNAME (AS PATH PARAM) (FOR THE LOGGED PLAYER)
@router.get("/nick/{nick}", status_code=status.HTTP_200_OK)
async def get_one_hero_by_nick(player: player_dependency, db: db_dependency, nick: str = Path()):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    result = db.query(Heroes).filter(Heroes.nick_name.ilike(f"%{nick}%")).filter(Heroes.owner_id == player.get("id")).all()
    return result
    # Return can be empty

# POST/CREATE (BY BODY)
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_hero(player: player_dependency, db: db_dependency, hero_body: HeroValidation = Body()):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    new_hero = Heroes(**hero_body.model_dump(exclude={"id"}), owner_id=player.get("id"))
    db.add(new_hero)
    db.commit()

# UPDATE WITH PUT (BY PATH) (FOR THE LOGGED PLAYER)
@router.put("/update/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_hero(player: player_dependency, db: db_dependency, hero_id: int = Path(ge=1), hero_body: HeroValidation = Body()):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).filter(Heroes.owner_id == player.get("id")).first()
    if hero_db is None:
        raise HTTPException(status_code=404, detail="Hero can't be found")
    hero_db.nick_name = hero_body.nick_name
    hero_db.full_name = hero_body.full_name
    hero_db.occupation = hero_body.occupation
    hero_db.powers = hero_body.powers
    hero_db.hobby = hero_body.hobby
    hero_db.type = hero_body.type
    hero_db.rank = hero_body.rank
    db.add(hero_db)
    db.commit()

# DELETE (BY ID AS PATH PARAM) (FOR THE LOGGED PLAYER)
@router.delete("/delete/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(player: player_dependency, db: db_dependency, hero_id: int = Path(gt=0)):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    hero_db = db.query(Heroes).filter(Heroes.id == hero_id).filter(Heroes.owner_id == player.get("id")).first()
    if hero_db is None:
        raise HTTPException(status_code=404, detail="Hero can't be found")
    db.delete(hero_db)
    db.commit()