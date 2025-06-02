from fastapi import HTTPException, APIRouter, Depends, Body
from starlette import status
from database import db_dependency
from models import Players
from routers.auth_router import player_dependency, bcrypt_context
from classes import ResetPasswordValidation

router = APIRouter(
    tags=["players"],
    prefix="/players"
)

# LOGGED PLAYER GETS HIS INFOS
@router.get("/", status_code=status.HTTP_200_OK)
async def get_player(player: player_dependency, db: db_dependency):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return db.query(Players).filter(Players.id == player.get("id")).first()
    # Return can be empty

# LOGGED PLAYER CAN CHANGE HIS PASSWORD
@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def reset_password(player: player_dependency, db: db_dependency, player_form_data: ResetPasswordValidation = Body()):
    if player is None:
        raise HTTPException(status_code=401, detail="Authentication failed")
    found_player = db.query(Players).filter(Players.id == player.get("id")).first()
    if not bcrypt_context.verify(player_form_data.old_pass, found_player.hashed_password):
        raise HTTPException(status_code=401, detail="Authentication failed")
    found_player.hashed_password = bcrypt_context.hash(player_form_data.new_pass)
    db.add(found_player)
    db.commit()