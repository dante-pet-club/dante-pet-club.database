import psycopg
import utils.statements
import pandas as pd


def build_insert_statement(statement: str, table_name: str, data: list[dict]) -> str:
    values_placeholders = []
    for value in data[0].keys():
        values_placeholders.append(f"%({value})s")
    keys_string = ", ".join(data[0].keys())
    values_string = ", ".join(values_placeholders)
    return statement % (table_name, keys_string, values_string)


def generic_insert(
    cur: psycopg.cursor, statement: str, table_name: str, data: list[dict]
):
    if len(data) == 0:
        return
    statement = build_insert_statement(statement, table_name, data)
    for entry in data:
        try:
            cur.execute(statement, entry)
        except Exception as e:
            print(e)
            print(entry)
            return


def parquet_insert(
    cur: psycopg.cursor, statement: str, table_name: str, df: pd.DataFrame
):
    statement = build_insert_statement(statement, table_name, [df.iloc[0].to_dict()])
    for index, entry in df.iterrows():
        try:
            cur.execute(statement, entry.to_dict())
        except Exception as e:
            print(e)
            print(entry)
            return


def generic_delete(cur: psycopg.cursor, table_name: str):
    delete_statement = utils.statements.delete_statement
    cur.execute(delete_statement % table_name)


if __name__ == "__main__":
    print(__name__)
