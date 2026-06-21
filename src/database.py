import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Inv3rter-23",
        database="pkdd_bank"
    )