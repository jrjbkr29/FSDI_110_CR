#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Create database tbales from SQLAlchemy Classes"""

from app import db

if __name__ =="__main__":
    db.create_all()
