class Calculadora():
    def __init__(self, x, y):
        self.x = x
        self.y = y



    def Adicao(self):
        res = self.x + self.y
        return res    
        

    def Sub(self):
        res = self.x - self.y
        return res      
    

    def Mult(self):
        res = self.x * self.y
        return res  
    
    def Div(self):
        res = self.x / self.y
        return res  
    
    def Tabuado(self, z):
        for i in range(13):
            res = f'{z} x {i} = {z*i}' 
            print(res)
    
if __name__ == '__main__':
    calculo = Calculadora(10, 5)
    res = calculo.Adicao()
    print(res)
    calculo.Tabuado(2)
    