import mariadb
from datetime import date


database = {
    'host': '172.18.4.58',
    'database': 'wip_inventory',
    'user': 'yura_admin',
    'password': 'Metallica24+',
    'port': 3306
}


def getWip(connection: dict, area: str, month: str) -> (dict, dict):
    # month = date.today().strftime("%m%y")
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
    con.close()
    wip = [list(i) for i in wip]
    wip = {i[10]: i for i in wip}

    inventario = [list(i) for i in inventario]
    inventario = {i[1]: i for i in inventario}
    return wip, inventario


def checkCode(code):
    length = len(code)
    start = code[0]
    if length == 10 and start == "4":
        return code
    elif start == "!" and length >= 17:
        return code[1:12]
    else:
        return "err"
