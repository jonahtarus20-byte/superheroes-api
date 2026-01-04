from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    # clear old data
    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()

    # add actors
    actors = [
        Hero(name="Robert Downey Jr.", super_name="Iron Man"),
        Hero(name="Chris Evans", super_name="Captain America"),
        Hero(name="Scarlett Johansson", super_name="Black Widow"),
        Hero(name="Chris Hemsworth", super_name="Thor"),
        Hero(name="Tom Holland", super_name="Spider-Man")
    ]

    # add skills
    powers = [
        Power(
            name="MCU Leadership",
            description="leading roles across many Marvel Cinematic Universe movies"
        ),
        Power(
            name="Action Performance",
            description="performing strong action scenes and physical fight sequences"
        ),
        Power(
            name="Fan Popularity",
            description="high popularity and global fan support across Marvel movies"
        )
    ]

    db.session.add_all(actors + powers)
    db.session.commit()

    # connect actors to skills
    hero_powers = [
        HeroPower(strength="Strong", hero_id=actors[0].id, power_id=powers[0].id),
        HeroPower(strength="Strong", hero_id=actors[1].id, power_id=powers[0].id),
        HeroPower(strength="Average", hero_id=actors[2].id, power_id=powers[1].id),
        HeroPower(strength="Strong", hero_id=actors[3].id, power_id=powers[2].id),
        HeroPower(strength="Average", hero_id=actors[4].id, power_id=powers[2].id)
    ]

    db.session.add_all(hero_powers)
    db.session.commit()

    print("Database seeded successfully")
