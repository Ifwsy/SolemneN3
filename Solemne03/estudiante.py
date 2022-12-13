from persona import Persona

class Estudiante(Persona):
    def __init__(self, n="", e="",c=""):
        super().__init__(n, e)
        self.__carrera=c
    
    def __str__(self):
        return super().__str__()+"Carrera: {}".format(self.__carrera)
    
    def GetCarrera(self):
        return self.__carrera
    def SetCarrera(self,c):
        self.__carrera=c