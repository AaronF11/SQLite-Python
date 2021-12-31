import sqlite3

connection = sqlite3.connect("src/database/records.db")

cursor = connection.cursor()