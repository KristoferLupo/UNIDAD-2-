import sqlite3
from curso.curso import Curso
def create_table():
    try:
        conn = sqlite3.connect("sqlite/prueba.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS CURSO(
                SIGLA VARCHAR(15) PRIMARY KEY,
                NOMBRE VARCHAR(50) NOT NULL,
                DOCENTE VARCHAR(250),
                FOREIGN KEY (DOCENTE) REFERENCES PERSONA (RUT)
                );
            """
        )

        conn.commit()
        conn.close()
    except Exception as e:
        print(e)


def insert_curso( curso : Curso ):
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO CURSO VALUES (?, ?, NULL)",
                (curso.sigla, curso.nombre)
            )
    except Exception as e:
        print(e)
    
    else:
        print("Se han ingresado los datos")

def listar_cursos(): 
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM CURSO;")
            lista_de_cursos = []
            for fila in cursor:
                curso = Curso(fila[0], fila[1])
                lista_de_cursos.append(curso)
            return lista_de_cursos
    except Exception as e:
        print(e)

