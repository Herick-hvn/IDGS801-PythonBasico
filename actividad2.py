class Calculator:
    def __init__(self):
        pass

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b
        

def main():
    calc = Calculator()
    while True:
        try:
            num1 = float(input("Dame el primer numero: "))
            num2 = float(input("Dame el segundo numero: "))
            operation = input("Que operacion haras (+, -, *, /, salir): ")
            if operation == "+":
                print(calc.suma(num1, num2))
            elif operation == "-":
                print(calc.resta(num1, num2))
            elif operation == "*":
                print(calc.multiplicacion(num1, num2))
            elif operation == "/":
                print(calc.division(num1, num2))
            elif operation == "salir":
                break
            else:
                print("Operacion invalida")
        except ValueError:
            print("")

if __name__ == '__main__':
    main()
