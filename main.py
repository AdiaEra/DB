import datetime
import sqlite3

import pandas as pd

from DB import cur, con


def add_client(clients_id: int):
    """
    Функция, позволяющая добавить нового клиента
    """
    if cur.fetchone() is None:
        try:
            cur.execute("INSERT INTO clients VALUES (?)", (clients_id,))
            con.commit()
            return 'Новый клиент добавлен'
        except sqlite3.IntegrityError:
            return 'Такой id есть в базе'


cl = 4465676980787


# print(add_client(cl))


def add_password(password, date):
    """
    Функция, позволяющая добавить новый пароль
    """
    if cur.fetchone() is None:
        try:
            cur.execute("INSERT INTO password VALUES (?, ?)", (password, date))
            con.commit()
            return 'Новый пароль добавлен'
        except sqlite3.IntegrityError:
            return 'Такой пароль есть в базе'


pasd = '2rfvg@@###566'


# print(add_password(pasd, datetime.datetime.now()))


def update_password(password, date):
    """
    Функция для обновления имеющегося пароля
    """
    pasd = '2rfvg@@###566'
    if cur.fetchone:
        try:
            a = "DELETE FROM password WHERE password = ?"
            cur.execute(a, (pasd,))
            con.commit()
            cur.execute("INSERT INTO password VALUES (?, ?)", (password, date))
            con.commit()
            return 'Пароль обновлён'
        except sqlite3.IntegrityError:
            return 'Такой пароль есть в базе'


new_pas = '##@@@@@787ghggvhfgf'


# print(update_password(new_pas, datetime.datetime.now()))


def all_id_csv():
    """
    Функция для записи id клиентов в csv файл
    """
    df = pd.read_sql('SELECT * from clients', con)
    df.to_csv('clients.csv', index=False)
    return df


# print(all_id_csv())


def delete_password():
    """
    Функция для удаления пароля
    """
    pasd = '##@@@@@787ghggvhfgf'
    a = "DELETE FROM password WHERE password = ?"
    cur.execute(a, (pasd,))
    con.commit()
    return 'Пароль удалён'


# print(delete_password())

def delete_id():
    """
    Функция для удаления id клиента
    """
    del_cl = 333345411111111111
    a = "DELETE FROM clients WHERE id = ?"
    cur.execute(a, (del_cl,))
    con.commit()
    return 'id клиента удалён'


# print(delete_id())
