from persona import Persona

class Docente(Persona):
    def __init__(self, n="", e="",s=""):
        super().__init__(n, e)
        self.__sueldo=s
    
    def __str__(self):
        return super().__str__()+"Sueldo: {}".format(self.__sueldo)

    def GetSueldo(self):
        return self.__sueldo
    def SetSueldo(self,s):
        self.__sueldo=s