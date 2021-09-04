from os import error
import sqlite3
from sqlite3.dbapi2 import Cursor
from typing import Text
banco = sqlite3.connect('dados_clientes.db')
cursor = banco.cursor()
""" ##cursor.execute("CREATE TABLE dados (nome text,idade integer, email text, cpf integer)");## """
""" cursor.execute("INSERT INTO dados VALUES('LAURO', 33, 'LA@gmail.com', 223392900) ");

banco.commit() """

""" cursor.execute("select * from dados")
print(cursor.fetchall()) """

cursor.execute ("DELETE FROM dados WHERE nome = LAURO")
banco.commit()
banco.close()
print("Os dados foram apagados")

except sqlite3.Error as erro:
    print("Erro ao processar operação:" erro)
