from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id = 0, origen_x = 0, origen_y = 0, destino_x = 0, destino_y=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.distancia = distancia_euclidiana(origen_x,origen_y,destino_x,destino_y)
       
    def __str__(self):
        return('Id : ' + str(self.__id) + '\n' + 'Origen en X :' + str(self.__origen_x) + '\n' + 
               'Origen en Y :' + str(self.__origen_y) + '\n' + 'Destino en X :' + str(self.__destino_x) + '\n' +
               'Destino en Y: ' + str(self.__destino_y) + '\n' + 'Distancia : ' + str(self.distancia) + '\n')
       
       
