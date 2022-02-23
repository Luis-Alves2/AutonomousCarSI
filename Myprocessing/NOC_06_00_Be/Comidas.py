# The "Comidas" class

class Comidinhas():

    def __init__(self, comidasIniciais):
        self.comidinhas = comidasIniciais
        
    # Method to update location
    def update(self):
        self.comidinhas +=1
    
    def getComidinhas(self):
        print("A comida foi coletada")
        print(self.comidinhas)
