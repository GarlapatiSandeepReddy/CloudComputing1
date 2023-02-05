import sqlite3

DATABASE = 'example.db'


def execute_query(query, args=()):
    conn = sqlite3.connect(DATABASE)
    cur = conn.execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows
execute_query("DROP TABLE IF EXISTS users")
execute_query("CREATE TABLE users (Username text,Password text,firstname text, lastname text, email text, count integer)")
