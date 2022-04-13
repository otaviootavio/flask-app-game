import sqlite3

from App import create

def create_db():
    connection = sqlite3.connect('database.db')
    with open('schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO devenvolvedoras (nome, site) VALUES (?,?)",
                ('Ola mundo!', 'Negocio')
                )
    

    connection.commit()
    connection.close()

create_db()