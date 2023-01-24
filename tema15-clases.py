
class OperasBas:

    #propiedades de la clase
    n1=0
    n2=0
    res=0

    #contructor de la clase

    def __init__(self, a,b):
        self.n1=a
        self.n2=b
        pass

    #metodos de la clase
    def suma(self):
        self.res = self.n1 + self.n2

   
def main():
    obj = OperasBas(3,2)
    obj.suma
