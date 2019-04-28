class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
        
    
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def propiedadPrivada(self, valor=None):#esto es un getter y un setter todo en uno
        if valor == None:
            #actua como getter
            return self.__propiedad_privada
        else:
            #actua como setter
            self.__propiedad_privada = valor
    
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada --> {} ".format(self.__propiedad_privada)
    
if __name__ == "__main__":
    c = ClaseConGetterySetter()
        
'''
Shell (aún no he añadido def propiedadPrivada)
>>> c.__propiedad_privada
Traceback (most recent call last):
  File "<pyshell>", line 1, in <module>
AttributeError: 'ClaseConGetterySetter' object has no attribute '__propiedad_privada'
>>> print(c)
ClaseConGetterySetter con propiedadPrivada --> None 
>>> c.getPropiedadPrivada()
>>> c.setPropiedadPrivada(24)
>>> c.getPropiedadPrivada()
24
>>> '''

'''
Shell (funcion propiedadPrivada añadida:)
print(c)
ClaseConGetterySetter con propiedadPrivada --> None 
>>> c.setPropiedadPrivada("un chalet con vistas")
>>> print(c)
ClaseConGetterySetter con propiedadPrivada --> un chalet con vistas 
>>> c.propiedadPrivada()
'un chalet con vistas'
>>> c.propiedadPrivada("Un chalet con vistas y piscina")
>>> c.propiedadPrivada()
'Un chalet con vistas y piscina'
>>>
'''