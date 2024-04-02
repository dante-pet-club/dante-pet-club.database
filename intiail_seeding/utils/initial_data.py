import datetime
from dateutil.relativedelta import relativedelta

# from faker import Faker
# import numpy as np

identification_type = [
    {
        "id": 1,
        "name": "cédula de  ciudadanía",
        "description": "ID for adults",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 2,
        "name": "tarjeta de identidad",
        "description": "ID for underage",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 3,
        "name": "NIT",
        "description": "ID for companies",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 3,
        "name": "Cédula de extranjería",
        "description": "ID for foreigners",
        "created_at": datetime.datetime.now(),
    },
]

status = [
    {
        "id": 1,
        "name": "active",
        "description": "user is currently active in platform",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 2,
        "name": "inactive",
        "description": "user is currently inactive in platform",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 3,
        "name": "blocked",
        "description": "user has been blocked",
        "created_at": datetime.datetime.now(),
    },
]

confirmation = [
    {
        "id": 1,
        "name": "false",
        "description": "Account created by another user, identity not confirmed.",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 2,
        "name": "email",
        "description": "Account confirmed through email.",
        "created_at": datetime.datetime.now(),
    },
    {
        "id": 3,
        "name": "ID",
        "description": "User and pet identity verified through ID document.",
        "created_at": datetime.datetime.now(),
    },
]

size = [
    {"size": "XS"},
    {"size": "S"},
    {"size": "M"},
    {"size": "L"},
    {"size": "XL"},
]

sex = [
    {"sex": "macho"},
    {"sex": "hembra"},
]

gender = [
    {"gender": "hombre"},
    {"gender": "mujer"},
    {"gender": "no binario"},
    {"gender": "otro"},
]