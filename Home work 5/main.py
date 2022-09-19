"""
Задача 1
"""
"""a = float(input ("введите число a = "))
b = float(input ("введите число b = "))
c = float(input ("введите число c = "))
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print ("yes")
else:
    print ("no")
"""

"""
Задача 2
"""

"""
a = float(input ("введите число a = "))
b = float(input ("введите число b = "))
c = float(input ("введите число c = "))
max = a
if b > max :
   max = b
if c > max :
   max = c
print (f"Большее число = {max}")
"""
"""
Задача 3
"""

number = int(input ("введите трехзначное число = "))
reversed_number = 0
if number >= 100 and number <= 999 :
    last = number % 10
    number = number // 10
    reversed_number = last
    last = number % 10
    number = number // 10
    reversed_number = reversed_number * 10
    reversed_number = reversed_number + last
    last = number % 10
    reversed_number = reversed_number * 10
    reversed_number = reversed_number + last
    print (f"Обратное число = {reversed_number}")
else:
    print ("wrong")
