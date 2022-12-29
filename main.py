"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(*args):
    total = sum(args)
    if total > 15:
        return max(args)
    elif total < 10:
        return min(args)
    else:
        for i in args:
            if i != max(args) and i != min(args):
                return i
    

print(devolver_distintos(int(input('Introduzca primer número: ')), int(input('Introduzca segundo número: ')), int(input('Introduzca tercer número: '))))
    