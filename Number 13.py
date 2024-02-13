import math
rad_small = int(input("Введите радиус слепой зоны: "))
rad_big = int(input("Введите радиус дальности приёма: "))
s_circle_small = math.pi * rad_small ** 2
s_circle_big = math.pi * rad_big ** 2
rad_answer = s_circle_big - s_circle_small
print(rad_answer)