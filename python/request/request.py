import mariadb
import datetime

def get_db_connection():
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=33066,
        database="maintenanceapp"
    )
    cur = conn.cursor()
    return cur, conn

def insert_in_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)

    conn.commit()
    add_id = cur.lastrowid
    conn.close()
    return add_id

def select_from_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)
    records = cur.fetchall()

    field_names = [i[0] for i in cur.description]
    result = []
    for record in records:
        element = {}
        for key, value in enumerate(record):
            if type(value) is datetime.datetime:
                element[field_names[key]] = value.strftime('%m/%d/%Y')
            else:
                element[field_names[key]] = value
        result.append(element)

    conn.close()
    return result

def delete_from_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)

    conn.commit()
    conn.close()

def update_from_db(requete, data=()):
    cur, conn = get_db_connection()
    
    cur.execute(requete, data)

    conn.commit()
    conn.close()