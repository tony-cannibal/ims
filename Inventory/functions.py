import mariadb
from datetime import date


database = {
    'host': '172.18.4.58',
    'database': 'wip_inventory',
    'user': 'yura_admin',
    'password': 'Metallica24+',
    'port': 3306
}


def getWip(connection, area):
    month = date.today().strftime("%m%y")
    con = mariadb.connect(**connection)
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM wip WHERE id LIKE %s AND area = %s;
                """, (month + "%", area))
    wip = cur.fetchall()

    cur.execute("""
    SELECT * FROM wip WHERE id LIKE %s AND area = %s;
                """, (month + "%", area))
    inventario = cur.fetchall()

    cur.close()
    wip = [list(i) for i in wip]
    lotes = [i[10] for i in wip]
    inventario = [list(i) for i in inventario]
    for i in lotes:
        print(i)
    return wip, lotes, inventario
