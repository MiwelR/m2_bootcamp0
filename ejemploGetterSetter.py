class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None

# Setter (fijar valor):
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor

# Getter (devuelve valor):
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
# Setter y Getter en un método:
    def propiedadPrivada(self, valor=None):
        if valor == None:
            #Actúa como getter
            return self.__propiedad_privada
        else:
            #Actúa como setter
            self.__propiedad_privada = valor
    
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
        
if __name__ == '__main__':
    c = ClaseConGetterySetter()