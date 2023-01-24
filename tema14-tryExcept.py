

num1=20
num2=0


try:
    tem=num1/num2
    pass
except ZeroDivisionError:
    print("Error en el progrma")
    pass
finally:
    print("siempre aparezco")