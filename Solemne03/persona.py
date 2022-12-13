class Persona():
    def __init__(self,n="",e=""):
        self.__nombre=n
        self.__edad=e
    
    def __str__(self):
        return "Nombre: {} Edad: {}".format(self.__nombre,self.__edad)
    
    def GetNombre(self):
        return self.__nombre
    def GetEdad(self):
        return self.__edad
    def SetNombre(self,n):
        self.__nombre=n
    def SetEdad(self,e):
        self.__edad=e