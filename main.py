import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30) #posicion y en el circuito lo ponemos privado para evitar modificaciones
    __colorTurtle = ('red', 'green', 'yellow', 'blue')
    
    def __init__(self, width, height):#propiedades principales como es la pantalla o circuito 
    
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startline = -width/2 + 20
        #posicion de salida de las tortugas +20 para dejar un margen
        self.__finishline = width/2 - 20
        #posicion de salida de las tortugas -20 para dejar un margen
        
        self.__createRunners()
    
    def __createRunners(self):#creado para separar la zona de propiedades de los corredores 
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape("turtle")
            #forma de tortuga y no flecha
            new_turtle.color(self.__colorTurtle[i])
            #cada tortuga tenga un color, si lo pones en esta posición no empiezan en color negro
            new_turtle.penup()
            #levanta el boli para que no pinte la tortuga
            new_turtle.setpos(self.__startline, self.__posStartY[i])
            
            self.corredores.append(new_turtle)
            
    
    def competir(self):
        
        hayGanador = False #esto no es un atributo no se puede invocar es una variable como la de las funciones
        
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6) #simulamos que tiramos un dado , numero aleatorio para avanzar
                tortuga.fd(avance) #le decimos a la tortuga que avance lo que haya resultado de random
                if tortuga.position()[0] >= self.__finishline: #tortuga.position() nos da la posicion en coordenadas (x,y) ponemos [0] para indicar la coordenada x
                    hayGanador = True
        
            
            
        
if __name__ == "__main__" :
    circuito = Circuito(640, 480)
    circuito.competir() #estoy invocando para que ejecute funcion competir
        
        