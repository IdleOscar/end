import psycopg2
from psycopg2 import OperationalError
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
 "postgres", "postgres", "123", "127.0.0.1", "5432"
)

create_users_table = """
CREATE TABLE IF NOT EXISTS Blog (
 id SERIAL PRIMARY KEY,
 author_name TEXT NOT NULL,
 title TEXT,
 intro TEXT,
 text TEXT,
 date TEXT
)
"""
def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
execute_query(connection, create_users_table)

insert_query = (
f"INSERT INTO Blog (author_name, title, intro, text, date) VALUES {'Aliaskar','Endterm','VERy HARD','NExt time i use VS CODE ', '31-10-2022'}"
)
connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query)