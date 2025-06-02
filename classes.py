from typing import List, Optional, Literal
from pydantic import BaseModel, Field, constr, field_validator

class Hero:
    id: int
    nick_name: str
    full_name: str
    occupation: List[str]
    powers: List[str]
    hobby: List[str]
    type: str
    rank: int
    def __init__(self, id, nick_name, full_name, occupation, powers, hobby, type, rank):
        self.id = id
        self.nick_name = nick_name
        self.full_name = full_name
        self.occupation = occupation
        self.powers = powers
        self.hobby = hobby
        self.type = type
        self.rank = rank

class HeroValidation(BaseModel):
    id: Optional[int] = Field(default=None, ge=0, description="ID is not needed on create")
    nick_name: str = Field(min_length=3)
    full_name: str = Field(min_length=3)
    occupation: List[constr(min_length=3)]
    powers: List[constr(min_length=3)]
    hobby: List[constr(min_length=3)]
    type: str = Field(min_length=3)
    rank: int = Field(ge=0, le=100)
    model_config = {
        "json_schema_extra": {
            "example": {
                "nick_name": "Percy",
                "full_name": "Percival Fredrickstein Von Musel Klossowski de Rolo III",
                "occupation": ["Aristocrat", "Ruler of Whitestone", "Member of Vox Machina"],
                "powers": ["Gunsmanship", "Craftsmanship", "Strength", "Speed"],
                "hobby": ["Designing and building new weapons like 'Bad News'", "Building weapons and gadgets"],
                "type": "Tragic Aristocrat",
                "rank": 63
            }
        }
    }

AllowedRoles = Literal["controller", "defender", "leader", "striker"]

class PlayerValidation(BaseModel):
    email: str = Field(description="Email address")
    username: str = Field(description="Pseudo")
    first_name: str = Field(description="First name")
    last_name: str = Field(description="Family name")
    password: str = Field(description="Password")
    role: AllowedRoles = Field(description="Role of the player. Should be either controller, defender, leader or striker")
    # PRE VALIDATOR
    @field_validator("role", mode="before")
    @classmethod
    def lower_case_role(cls, val: str) -> str:
        return val.lower()
    # CUSTOMIZATION OF DISPLAYED INFOS IN SWAGGER MODEL
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "player@example.com",
                "username": "thechampion",
                "first_name": "Alex",
                "last_name": "Storm",
                "password": "strongpassword123",
                "role": "controller"
            }
        }
    }

class Token(BaseModel):
    access_token: str
    token_type: str

class ResetPasswordValidation(BaseModel):
    old_pass: str
    new_pass: str