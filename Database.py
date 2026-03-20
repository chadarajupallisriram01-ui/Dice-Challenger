import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import sqlite3 as sq

def get_connection():
    return sq.connect("Database.db",check_same_thread=False)
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""Create Table if not exists Won(
                Mobile integer primary key,
                Name text not null,
                status text not null,
                created_at timestamp
                )""")
create_tables()
print("Database created")