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
    