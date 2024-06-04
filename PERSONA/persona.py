class Persona ():
    def __init__(self,rut,nombre,apellido,fecha_nacimineto,tipo) -> None:
        self.rut = rut 
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimineto = fecha_nacimineto
        self.__tipo = tipo
    @property
    def rut (self):
        return self.__rut
    @rut.setter
    def rut (self,rut):
        print ("hola")
        self.__rut = rut 

    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter
    def nombre (self,nombre):
        self.__nombre = nombre

    @property
    def apellido (self):
        return self.__apellido
    @apellido.setter
    def apellido (self,apellido):
        self.__apellido = apellido 

    @property
    def fecha_nacimiento (self):
        return self.__fecha_nacimineto
    @fecha_nacimiento.setter
    def fecha_nacimiento (self,fecha_nacimiento):
        self.__fecha_nacimineto = fecha_nacimiento 
    
    @property
    def tipo (self):
        return self.__tipo
    @tipo.setter
    def tipo (self,tipo):
        self.__tipo = tipo

    def __str__(self) -> str:
        return f"""
    rut = {self.__rut}
    nombre = {self.__nombre}
    apellido = {self.__apellido}
    fecha_nacimiento = {self.__fecha_nacimineto}
    tipo = {self.__tipo}
    """

est=Persona("h","h","h","h","docente")