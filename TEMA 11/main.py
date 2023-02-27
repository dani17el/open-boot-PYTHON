import sqlite3

db_connection = sqlite3.connect('ej1.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Maria', 'Lopez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Dani', 'Ruiz')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Aaron', 'Guanilo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Nancy', 'Perez')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Fatima', 'Cuenca')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'Josep', 'Grande')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'Christian', 'Ledesma')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'Omar', 'Ledesma')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Maria'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()