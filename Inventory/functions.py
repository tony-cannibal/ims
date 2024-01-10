import mariadb
# from datetime import date


database = {
    'host': '172.18.4.58',
    'database': 'wip_inventory',
    'user': 'yura_admin',
    'password': 'Metallica24+',
    'port': 3306
}


def getWip(connection: dict, area: str, month: str) -> (dict, dict):
    con = mariadb.connect(**connection)
    cur = con.cursor()

    cur.execute("""
    SELECT * FROM wip WHERE id LIKE %s AND area = %s;
                """, (month + "%", area))
    wip = cur.fetchall()

    cur.close()
    con.close()
    wip = [list(i) for i in wip]
    wip = {i[10]: i for i in wip}

    return wip


def getInventory(connection, area, month):
    con = mariadb.connect(**connection)
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM inventario WHERE id LIKE %s AND area = %s;
                """, (month + "%", area))
    inventario = cur.fetchall()
    cur.close()
    con.close()
    inventario = [list(i) for i in inventario]
    inventario = {i[1]: i for i in inventario}
    return inventario


def checkCode(code):
    if code == "":
        return "err"
    length = len(code)
    start = code[0]
    if code == "":
        return "err"
    if length == 10 and start == "4":
        return code
    elif start == "!" and length >= 17:
        return code[1:11]
    else:
        return "err"


def captureRecord(record, mes, connection):
    con = mariadb.connect(**connection)
    cur = con.cursor()
    cur.execute("""
    INSERT INTO inventario(
        id, lote, modelo, item, num_parte, cantidad, area)
        VALUES(
        %s, %s, %s, %s, %s, %s, %s
            );""", (
                record[0], record[1], record[2],
                record[3], record[4], record[5], record[6]
                ))
    con.commit()
    cur.close()
