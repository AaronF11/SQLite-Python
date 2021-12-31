from connection import *

cursor.execute("CREATE TABLE IF NOT EXISTS records"\
    "(MATRICULA VARCHAR(7), NOMBRE VARCHAR(150), APELLIDOS VARCHAR(150), CORREO_INSTITUCIONAL VARCHAR(150))")

''' cursor.execute("INSERT INTO info VALUES"\
    "('a', 'b', 'c', 'd')") '''

connection.commit()

connection.close()