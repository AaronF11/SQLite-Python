from connection import *

cursor.execute("CREATE TABLE IF NOT EXISTS records"\
    "(MATRICULA VARCHAR(7), NOMBRE VARCHAR(150), APELLIDOS VARCHAR(150), CORREO INSTITUCIONAL VARCHAR(150))")

connection.commit()

connection.close()