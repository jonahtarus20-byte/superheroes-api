MARVEL STUDIO ACTORS API
Date, 2026/01/03
By JONAH TARUS
Description

This is a Flask REST API for managing Marvel Studio actors and their powers.
The API allows users to view heroes (actors), view powers, assign powers to heroes, and update power descriptions.
It is built for learning backend development, databases, and RESTful APIs.

Installation

I used git clone to be able to download the documents in the GitHub.

Installation Requirements

Git
Python 3
Virtual Environment (venv)

Installation instruction
git clone git@github.com:jonahtarus20-byte/superheroes-api.git
cd superheroes-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask db upgrade
flask run

API Endpoints

GET /heroes

GET /heroes/:id

GET /powers

GET /powers/:id

PATCH /powers/:id

POST /hero_powers

Technologies used

Python
Flask
Flask SQLAlchemy
Flask Migrate
SQLite
Git & GitHub

Support and contact details

GitHub: https://github.com/jonahtarus20-byte

Copyright (c) 2026.
