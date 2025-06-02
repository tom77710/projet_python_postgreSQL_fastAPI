from typing import List
from classes import Hero
import csv

HEROES: List[Hero] = [
    Hero(
        id=1,
        nick_name="Gale",
        full_name="Gale Dekarios",
        occupation=["Wizard", "Adventurer", "Deity"],
        powers=["Magical prowess", "High intelligence", "Charisma"],
        hobby=["Studying magic", "Drinking", "Cooking"],
        type="Wizard",
        rank=54
    ),
    Hero(
        id=2,
        nick_name="Doric",
        full_name="Doric",
        occupation=["Druid", "Adventurer"],
        powers=["Combat skills", "Shapeshifting"],
        hobby=["Stealing with Edgin, Simon, and Holga."],
        type="Druid",
        rank=71
    ),
    Hero(
        id=3,
        nick_name="Ed",
        full_name="Edgin Darvis",
        occupation=["Thief", "Adventurer", "Harper agent"],
        powers=["Magical skills", "Strategizing", "High-level Intelligence", "Charisma"],
        hobby=["Playing music"],
        type="Thief",
        rank=68),
    Hero(
        id=4,
        nick_name="Ho-Ho",
        full_name="Holga Kilgore",
        occupation=["Member of the Elk tribe", "Adventurer", "Thief"],
        powers=["Great strength", "Dancing skills"],
        hobby=["Hanging out with Edgin"],
        type="Amazonian Brute",
        rank=85
    ),
    Hero(
        id=5,
        nick_name="Xenk",
        full_name="Xenk Yendar",
        occupation=["Paladin", "Adventurer"],
        powers=["Sensing evil", "Magical skills", "Fighting skills", "Charisma"],
        hobby=["Helping people", "Fighting evil"],
        type="Knight",
        rank=95
    ),
    Hero(
        id=6,
        nick_name="Uncle Forge",
        full_name="Forge Fitzwilliam",
        occupation=["Lord of Neverwinter", "Prisoner"],
        powers=[
            "Charisma", "Agility", "Stealth", "Manipulation",
            "Deception", "Investigation skills", "Intelligence", "Forgery skills"
        ],
        hobby=["Conspiracy", "Usurpation", "Abuse of power"],
        type="Opportunist",
        rank=80
    ),
    Hero(
        id=7,
        nick_name="The would-be sorcerer",
        full_name="Simon Aumar",
        occupation=["Sorcerer", "Thief"],
        powers=["Magic", "Spellcasting", "Arcane Knowledge"],
        hobby=["Stealing with Edgin, Doric, and Holga."],
        type="Insecure Sorcerer",
        rank=82
    ),
    Hero(
        id=8,
        nick_name="The red wizard",
        full_name="Sofina",
        occupation=[
            "Member of the Red Wizards of Thay",
            "Forge Fitzwilliam's right hand (formerly)"
        ],
        powers=["Dark magic", "Extreme intelligence", "Immortality", "Bilingualism"],
        hobby=[
            "Conspiracy", "Terrorism", "Attempted populicide",
            "Unlawful imprisonment", "Animal cruelty", "Mass murder", "Property damage"
        ],
        type="Priestess",
        rank=85
    ),
    Hero(
        id=9,
        nick_name="Zulkir of Necromancy",
        full_name="Szass Tam",
        occupation=[
            "Leader of the Red Wizards of Thay",
            "Ruler of Thaymount"
        ],
        powers=["Necromancy", "Mastery of dark magic", "Leadership", "Manipulation"],
        hobby=[
            "Corruption", "Slavery", "Torture", "Abuse of power",
            "Brainwashing", "Defilement", "Extortion"
        ],
        type="Lich",
        rank=100
    )
]

# CREATE A CSV FILE FROM THE ABOVE
def format_array(py_list):
    return '{' + ','.join(f'"{item}"' for item in py_list) + '}'

with open("heroes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # HEADERS
    writer.writerow(["nick_name", "full_name", "occupation", "powers", "hobby", "type", "rank"])
    # DATA
    for hero in HEROES:
        writer.writerow([hero.nick_name, hero.full_name, format_array(hero.occupation), format_array(hero.powers),
                         format_array(hero.hobby), hero.type, hero.rank])

 # PSQL COMMAND TO IMPORT THE CSV FILE (DONT USE PGADMIN, ITS CRAP) AND INSTRUCTIONS :
 # PRODUCE THE FILE WITH F5
 # PUT THE LOCAL FILE IN HOME DIRECTORY AND APPLY FULL ACCESS RIGHTS (ALSO TO TOP FOLDER IF NECESSARY)
 # ENTER PSQL WITH ; sudo -u postgres psql.
 # LOG TO THE RIGHT DB
 # \copy public.heroes (nick_name, full_name, occupation, powers, hobby, type, rank) FROM '/your/directory/heroes.csv' DELIMITER ',' CSV HEADER ENCODING 'UTF8' QUOTE '"' ESCAPE '''';