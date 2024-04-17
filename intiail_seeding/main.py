import psycopg
from utils import initial_data as dt
from utils import statements
from utils import utils as ut
from utils import connection_strings

db_name = "dante_pet_club"

connection_string = connection_strings.AZURE
print(connection_string)
connection_string["dbname"] = db_name
print(connection_string)

insert_statement = statements.insert_statement


def batch_insert(cur: psycopg.cursor):
    ut.generic_insert(
        cur, insert_statement, "identification_type", dt.identification_type
    )
    ut.generic_insert(cur, insert_statement, "status", dt.status)
    ut.generic_insert(cur, insert_statement, "confirmation", dt.confirmation)
    ut.generic_insert(cur, insert_statement, "size", dt.size)
    ut.generic_insert(cur, insert_statement, "sex", dt.sex)
    ut.generic_insert(cur, insert_statement, "blob", dt.blob)
    ut.generic_insert(cur, insert_statement, "gender", dt.gender)
    ut.generic_insert(cur, insert_statement, "hobby", dt.hobby)
    ut.generic_insert(cur, insert_statement, "coat", dt.coat)
    ut.generic_insert(cur, insert_statement, "avatar", dt.avatar)

    ut.parquet_insert(cur, insert_statement, "country", dt.country)
    ut.parquet_insert(cur, insert_statement, "state", dt.state)
    ut.parquet_insert(cur, insert_statement, "city", dt.city)

    ut.generic_insert(cur, insert_statement, "owner", dt.owner)
    ut.generic_insert(cur, insert_statement, "dog", dt.dog)
    ut.generic_insert(cur, insert_statement, "dog_owner", dt.dog_owner)


def batch_delete(cur: psycopg.cursor):
    # Stage 3
    ut.delete_restart(cur, "dog_owner")
    ut.delete_restart(cur, "owner")
    ut.delete_restart(cur, "dog")

    ut.generic_delete(cur, "city")
    ut.generic_delete(cur, "state")
    ut.generic_delete(cur, "country")

    ut.delete_restart(cur, "gender")
    ut.delete_restart(cur, "sex")
    ut.delete_restart(cur, "size")
    ut.delete_restart(cur, "coat")
    ut.delete_restart(cur, "hobby")
    ut.delete_restart(cur, "avatar")
    ut.delete_restart(cur, "blob")

    ut.generic_delete(cur, "confirmation")
    ut.generic_delete(cur, "status")
    ut.generic_delete(cur, "identification_type")


with psycopg.connect(**connection_string) as conn:
    with conn.cursor() as cur:

        batch_delete(cur)
        batch_insert(cur)

        # conn.commit()
