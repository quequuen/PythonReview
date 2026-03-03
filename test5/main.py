import os
from datetime import datetime as dt, timedelta
from classes import Animal
from classes import VaccinRecord

base_path = "./test5/data"

if os.path.isdir(base_path):
    os.mkdir(base_path)

records = {}


while True:
    animal_id = input("동물 ID:")
    if animal_id == "":
        break
    if animal_id not in records:
        records[animal_id] = None










