import psycopg
import datetime
from faker import Faker
from utils import dummy_data
from utils import statements
from utils import utils as ut
from utils import connection_strings

db_name = "finale_app_dev"


connection_string = connection_strings.AZURE

# finale_app_connection_dict = {
#     "dbname": db_name,
#     "user": "alvarohc777",
#     "password": "finale-app#1",
#     "port": "5432",
#     "host": "finale-dev-app.postgres.database.azure.com",
# }
# finale_app_connection_dict = {
#     "dbname": "finale_app_dev",
#     "user": "postgres",
#     "port": "5432",
#     "host": "localhost",
# }


def batch_insert(curr: psycopg.cursor):
    # # Stage 1
    ut.generic_insert(
        cur, insert_statement, "identification_type", dummy_data.identification_type
    )
    ut.generic_insert(cur, insert_statement, "user_type", dummy_data.user_type)
    ut.generic_insert(cur, insert_statement, "status", dummy_data.status)
    ut.generic_insert(cur, insert_statement, "confirmation", dummy_data.confirmation)

    # city, country, continent
    ut.generic_insert(cur, insert_statement, "continent", dummy_data.continent)
    ut.generic_insert(cur, insert_statement, "country", dummy_data.country)
    ut.generic_insert(cur, insert_statement, "city", dummy_data.city)

    # # Stage 2
    ut.generic_insert(cur, insert_statement, "season", dummy_data.season)
    ut.generic_insert(cur, insert_statement, "user", dummy_data.user)
    ut.generic_insert(cur, insert_statement, "person", dummy_data.person)
    ut.generic_insert(cur, insert_statement, "organization", dummy_data.organization)

    # # Stage 3
    ut.generic_insert(cur, insert_statement, "role", dummy_data.role)


def batch_delete(cur: psycopg.cursor):
    # Stage 3
    ut.generic_delete(cur, "role")

    # Stage 2
    ut.generic_delete(cur, "person")
    ut.generic_delete(cur, "organization")
    ut.generic_delete(cur, "season")
    ut.generic_delete(cur, "user")

    # city, country, continent

    ut.generic_delete(cur, "city")
    ut.generic_delete(cur, "country")
    ut.generic_delete(cur, "continent")

    # Stage 1
    ut.generic_delete(cur, "identification_type")
    ut.generic_delete(cur, "user_type")
    ut.generic_delete(cur, "confirmation")
    ut.generic_delete(cur, "status")


fake = Faker()

insert_statement = statements.insert_statement


with psycopg.connect(**connection_string) as conn:
    with conn.cursor() as cur:
        pass
        # Insert Statements
        batch_insert(cur)
        conn.commit()
