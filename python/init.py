import mariadb
import sys
import re

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=33066,
        database="maintenanceapp"
    )
    cur = conn.cursor()
    #code ici

    with open('sql_file/init.sql') as f:
        fichier = f.read()
        lines = fichier.split(";")
        for index, line in enumerate(lines):
            if (line != ""):
                line = line.replace("\n", "")
                line = re.sub("\s+", " ", line)
                texte = cur.execute(line)

    with open('sql_file/create.sql') as f:
        fichier = f.read()
        lines = fichier.split(";")
        for index, line in enumerate(lines):
            if (line != ""):
                line = line.replace("\n", "")
                line = re.sub("\s+", " ", line)
                texte = cur.execute(line)
    conn.commit()
    conn.close()

except mariadb.Error as e:
    print(f"Erreur lors de la connection à la base de données: {e}")
    sys.exit(1)