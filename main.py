import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30) #posicion y en el circuito lo ponemos privado para evitar modificaciones
    __colorTurtle = ('red', 'green', 'yellow', 'blue')
    
    def __init__(self, width, height):
    
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startline = -width/2 + 20
        #posicion de salida de las tortugas +20 para dejar un margen
        self.__finishline = width/2 - 20
        #posicion de salida de las tortugas -20 para dejar un margen
        
        
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
        
if __name__ == "__main__" :
    circuito = Circuito(640, 480)
        
        