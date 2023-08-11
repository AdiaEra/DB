import sqlite3 as sq


with sq.connect("EHO.db") as con:
    cur = con.cursor()

    def delete_tab_clients():
        """
        Функция удаления таблицы clients
        """
        cur.execute("""DROP TABLE IF EXISTS clients""")
        return 'Таблица clients удалена'

    # print(delete_tab_clients())

    def create_tab_clients():
        """
         Функция создания таблицы clients
        """
        cur.execute("""CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY
            )""")
        return 'Таблица clients создана'

    # print(create_tab_clients())


    def delete_tab_password():
        """
        Функция удаления таблицы password
        """
        cur.execute("""DROP TABLE IF EXISTS password""")
        return 'Таблица password удалена'

    # print(delete_tab_password())

    def create_tab_password():
        """
        Функция создания таблицы password
        """
        cur.execute("""CREATE TABLE IF NOT EXISTS password(
            password TEXT PRIMARY KEY,
            date NUMERIC
            )""")
        return 'Таблица password создана'

    # print(create_tab_password())