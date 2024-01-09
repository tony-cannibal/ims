import pandas as pd
import mariadb
from datetime import date


wip = pd.read_excel("WIP 2023-10-31 H01M05.XLSX").values.tolist()

database = {
    'host': '172.18.4.58',
    'database': 'wip_inventory',
    'user': 'yura_admin',
    'password': 'Metallica24+',
    'port': 3306
}

columns = [
    0, 3, 5, 6, 7,
    8, 9, 10, 11,
    18, 21, 23, 24
]


def insertIntoDb(wip, columns, connection):
    '''Insert wip data into database.'''
    today = date.today().strftime("%m%y")

    area = {
        "M152": "M1",
        "M252": "M2",
    }
    con = mariadb.connect(**connection)
    cur = con.cursor()
    for i in wip:
        cur.execute("""
                INSERT INTO wip(
                    id, centro, lugar_de_elaboracion, modelo,
                    grupo_artic_externo, material, revicion, unidad,
                    feeder_21700, feeder_21800, lote, qty, item, ranking,
                    area)
                VALUES(
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s);
                    """, (
            today + str(i[18]), i[columns[0]], i[columns[1]],
            i[columns[2]], i[columns[3]], i[columns[4]], i[columns[5]],
            i[columns[6]], i[columns[7]], i[columns[8]], i[columns[9]],
            i[columns[10]], i[columns[11]], i[columns[12]],
            area[i[3]]
        ))
    con.commit()


if __name__ == "__main__":
    insertIntoDb(wip, columns, database)
