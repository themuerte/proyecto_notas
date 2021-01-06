import mysql.connector

def connector():
    database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Qwsxzaqwedc1!',
    database = 'master_python',
    port = 3306

    )

    cursor = database.cursor(buffered=True)

    return[database, cursor]