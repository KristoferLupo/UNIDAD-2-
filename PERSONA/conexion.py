import sqlite3
from PERSONA.persona import Persona
def create_table():
    try:
        conn = sqlite3.connect("sqlite/prueba.db")
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS PERSONAS(
                RUT VARCHAR(15) PRIMARY KEY,
                NOMBRE VARCHAR(50) NOT NULL,
                APELLIDO VARCHAR(50) NOT NULL,
                FECHA_NACIMIENTO DATE NOT NULL,
                TIPO VARCHAR (10) NOT NULL 
                );
            """
        )
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
    

def insert_persona(persona: Persona):
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO PERSONAS VALUES (?, ?, ?, ?, ?)",
                (persona.rut, persona.nombre, persona.apellido,
                 persona.fecha_nacimiento, persona.tipo)
            )
    except Exception as e:
        print(e)
    
    else:
        print("Se han ingresado los datos")


def listar_personas(tipo): 
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PERSONAS WHERE TIPO = (?);" , (tipo,))
            lista_de_personas = []
            for fila in cursor:
                persona = Persona(fila[0], fila[1], fila[2], fila[3], fila[4])
                lista_de_personas.append(persona)
            return lista_de_personas
    except Exception as e:
        print(e)

def asignar_docente(rut,sigla):
    try:
        with sqlite3.connect("sqlite/prueba.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE CURSO SET (DOCENTE) = ? WHERE (SIGLA) = ? " , (rut, sigla,))
            lista_de_personas = []
            for fila in cursor:
                Persona = Persona(fila[0])
                lista_de_personas.append(Persona)
            return lista_de_personas
            
    except Exception as e:
        print(e)


