import sympy as sp
#Declarando valores iniciales de x, a, h
valorX = float(sp.pi/3)
a = float(sp.pi/4)
h = valorX - a
#Variable donde se acumula las operaciones de la serie
s = 0
#Declarando la variable de la funcion y la funcion
x = sp.symbols('x', real=True)
fx = sp.sin(x)
#Resultado evaluado en el valor de x
valorFx = sp.sin(valorX)
#Variable del orden hasta el que deseamos operar
numOrden = 5
#Ciclo de la serie y sus operacioens
for i in range(0, numOrden):
    #Funcion de sympy que permite derivar y evaluar con respecto a la variable a
    df = sp.diff(fx, x, i).subs(x, a)
    #Suma de los resultados obtenidos
    s+=(df/sp.factorial(i))*(h**i)
    print(f'Valor obtenido en orden {i} = {s}')
print(f"""
Valor obtenido de sen(pi/3) = {valorFx}
Valor obtenido tras {i} evaluaciones = {s}
""")

    