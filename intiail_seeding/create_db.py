import psycopg
import subprocess

from utils import connection_strings


db_name = "dante_pet_club"
sql_file = "DogClubApp.sql"
host = "finale-dev-app.postgres.database.azure.com"

connection_string = connection_strings.AZURE_FINALE_APP

with psycopg.connect(autocommit=True, **connection_string) as conn:
    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE IF EXISTS {db_name}")
        cur.execute(f"CREATE DATABASE {db_name}")

psql_restore_cmd = (
    f"psql -U alvarohc777 -h {host} -d {db_name} -W -f ./schemas/{sql_file}"
)

powershell_command = "powershell.exe"
subprocess.run(f"{powershell_command} -c {psql_restore_cmd}", shell=True)

# psql_restore_cmd = "psql -U alvarohc777 -h finale-dev-app.postgres.database.azure.com -d finale_app_dev -W -f ./schemas/FinaleAppDev.sql"
# subprocess.run(psql_restore_cmd)
