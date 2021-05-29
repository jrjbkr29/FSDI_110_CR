#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Create database tables from SQLAlchemy Classes"""

from app import db
from database import User

def create_my_user(first_name, last_name, hobbies):
    """Creates users"""
    db.session.add(
        User(
            first_name=first_name,
            last_name=last_name,
            hobbies=hobbies
        )
    )
    db.session.commit()

if __name__ == "__main__":
    create_my_user("Johnny", "Jimenez", "Mechanic, family time, learning something new")
    users = User.query.all()
    print(users)
    create_my_user("Mayla", "Jimenez", "Playing with Everly")
    user = User.query.filter_by(first_name ="Mayla").first()
    print(user)
