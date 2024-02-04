#mini calculadora

#parte 1:
#le damos las opciones
eleccion = int(input('''
Mini Calculadora
Escriba un numero segun la operacion a realizar:
1-Suma
2-Resta
3-Multiplicacion
4-Division
elgia una: '''))
print('...........................')

#parte 2 
#si elije la 1 vamos a sumar todo lo que ponga
if eleccion == 1:
    print('Haz seleccionado la suma')
    a = float(input('introduzca el primer numero: '))
    b = float(input('introduzca el segundo numero: '))
    resultado = a + b
    print(f'resultado de la suma es: {resultado}')

#si elije la 2 vamo a entrar a restar ahora
elif eleccion == 2:
    print('Haz seleccionado resta')
    a = float(input('introduzca el primer numero: '))
    b = float(input('introduzca el segundo numero: '))
    resultado = a - b
    print(f'resultado de la resta es: {resultado}')

#si elije 3 vamo a ponernos a joder con multiplicaciones que asco
elif eleccion == 3:
    print('Haz seleccionado multiplicacion')
    a = float(input('introduzca el primer numero: '))
    b = float(input('introduzca el segundo numero: '))
    resultado = a * b
    print(f'resultado de la multiplicacion es: {resultado}')

#si elije la 4 lo peor division wakala
elif eleccion == 4:
    print('Haz seleccionado division')
    a = float(input('introduzca el divisor: '))
    b = float(input('introduzca el dividendo: '))
    resultado_cociente = a / b
    resultado_resto = a % b
    print(f'el cociente de la division es {resultado_cociente}')
    print(f'el resto de la divison es: {resultado_resto}')

#parte 3
#si es medio payaso le ponermos un error pa que se ria ahi
else:
    print('introduzca un numero valido')