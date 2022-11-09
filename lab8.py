import math
# Функция возвращает решение уравнения в виде списка
def SquareEquation(a, b, c):
    # Вложенная функция Disc() вычисления дискриминанта
    def Disc(a, b, c):
        d = b*b-4*a*c
        return d

    # Вычислить дискриминант
    D = Disc(a, b, c)

    if D>=0:
        x1 = (-b - math.sqrt(D))/(2*a)
        x2 = (-b + math.sqrt(D))/(2*a)
        return [x1, x2]
    else:
        return None

# Вызвать функцию для решения уравнения 2*x^2+3*x-5=0
#Функцию вызываем впринте
Res = SquareEquation(2, 3, -5)

if Res!=None:
    print('Result = ', Res)
else:
    print('The equation has no roots')