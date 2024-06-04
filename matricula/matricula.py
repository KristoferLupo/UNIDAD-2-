import sqlite3

def create_table():
    try:
        conn = sqlite3.connect("sqlite/prueba.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS MATRICULA(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                SIGLA VARCHAR(12),
                RUT VARCHAR(12),
                FOREIGN KEY (SIGLA) REFERENCES CURSO (SIGLA),
                FOREIGN KEY (RUT) REFERENCES PERSONAS (RUT)
                );
            """
        )

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)

def asignar_matricula(sigla,rut):
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO MATRICULA VALUES (NULL,?,?); ",
                (sigla, rut ,)
            )
    except Exception as e:
        print(e)
    
    else:
        print("Se han ingresado los datos")