from curso.conexion import create_table as Crear_curso, insert_curso , listar_cursos
from PERSONA.conexion import create_table as persona,insert_persona , listar_personas, asignar_docente
from matricula.matricula import create_table as matricula, asignar_matricula
from PERSONA.persona import Persona 
from curso.curso import Curso
persona()
Crear_curso()
matricula()

ESPACIO = 10

while True:
    print("\n")
    print("="*ESPACIO, "Menu Principal", "="*ESPACIO)
    print("""
    1) - Registrar alumno
    2) - Registrar docente
    3) - Registrar curso
    4) - Asignar docente
    5) - Matricular alumno
    6) - Listar alumnos
    7) - Listar docentes
    8) - Listar cursos
    9) - Salir
    """)

    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        Rut = input ("Ingresar Rut: ")
        nombre = input("Ingresar Nombre: ")
        apellido = input("Ingresar Apellido: ")
        fecha_nacimineto = input("Ingresar Fecha de Nacimiento: ")
        tipo_estudiante = "Estudiante"    
        personas = Persona (Rut,nombre,apellido,fecha_nacimineto,tipo_estudiante) 
        insert_persona (personas)

    if opcion == 2:
        Rut = input ("Ingresar Rut: ")
        nombre = input("Ingresar Nombre: ")
        apellido = input("Ingresar Apellido: ")
        fecha_nacimineto = input("Ingresar Fecha de Nacimiento: ")
        tipo_docente = "Docente"    
        personas = Persona (Rut,nombre,apellido,fecha_nacimineto,tipo_docente) 
        insert_persona (personas)

    if opcion == 3:
        sigla = input ("REGISTRO DEL CURSO: ")
        nombre = input("Ingresar Nombre: ")
        cursos = Curso (sigla,nombre) 
        insert_curso (cursos)

    if opcion == 4:
        print("")
        print("CURSOS")
        cursos = (listar_cursos())
        for curso in cursos : print (curso)
        docentes = listar_personas("Docente")
        input ("APRIETE PARA VER LOS DOCENTES")
        print("DOCENTES")
        for docente in docentes : print (docente) 
        sigla = input("Ingrese la sigla: ")
        rut = input("Ingresar el rut: ")
        asignar_docente (rut,sigla)
        print("SE HA AÑADIDO UN NUEVO DOCENTE AL RAMO")

    if opcion == 5:
        print("")
        print("CURSOS")
        cursos = (listar_cursos())
        for curso in cursos : print (curso)
        estudiantes = listar_personas("Estudiante")
        input ("PULSE CUALQUIER BOTON PARA CONTINUAR")
        print("Estudiantes")
        for estudiante in estudiantes : print (estudiante)
        sigla =input("INGRESE LA SIGLA DEL CURSO A MATRICULAR: ")
        rut = input("INGRESE EL RUT DEL ESTUDIANTE A MATRICULAR: ")
        asignar_matricula (sigla, rut)
        print("SE HA MATRICULADO EXITOSANENTE")

        
    if opcion == 6:
        estudiantes = listar_personas("Estudiante")
        for estudiante in estudiantes : print (estudiante)

    if opcion == 7:
        docentes = listar_personas("Docente")
        for docente in docentes : print(docente)
    if opcion == 8:
        cursos = (listar_cursos())
        for curso in cursos : print (curso)

    if opcion == 9: 
        break
