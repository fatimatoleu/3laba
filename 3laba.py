#1)	Написать программу используя цикл for и while.
name = "Salem alem!"
for i in name:
 print(i)
#Например я хочу вывести нашу фразу 5 раз, что нам необходимо сделать? 
name = "Salem alem!"
for i in range(1,11):
 print(name)
#цикл while
i = 1
while i<=10:
    print(i)
    i=i+1
#цикл while
i = 1
while i<=10:
    print(i)
    i=i+1
    break
#цикл while
i = 1
while i<=10:
    if i!=5:
     print(i)
    i=i+1
    continue
#цикл while
i = 1
while 1==1:
    print("Бесконечный цикл")
#2) используя функцию range() сделать список. в функцию range() введите данные с разными типами и выведите на экран в разных примерах.
for number in range(1,11):#первое число это начинающее число, последняя заканчивающаю
  print(number)#первая и последняя включена
x=list(range (1,11))
print(x)
for number in range(1,11,13):
    print(number)
friends_list = ["Нурали", "Нұрғаным","Қасым", "Дильзат", "Зейнеп", "Алена", "Аймұрат", "Мадина", "Алихан", "Санжар"]
for invite in range(1, len(friends_list),2 ):
     print({friends_list[invite].title()} )
#3) используйте функции randint() randrange() random() enumerate()  в своей программе 
print("Выбирите число, и получите в подарок упаковку чая!")
from random import randrange

tea_list = ['ЧЕРНЫЙ ЧАЙ', 'ЗЕЛЕНЫЙ ЧАЙ', 'БЕЛЫЙ ЧАЙ', 'УЛУН', 'ЧАЙ МАТЕ']

# получаем случайный номер индекса
i = randrange(len(tea_list))
item = tea_list[i]
# Выбераем элемент, используя порядковый номер
print("Случайно выбранная упаковка: ", tea_list[i], "находится под порядковым номером:", i, "Поздравляем с выигрышем!")
import random

number_list = [10, 20, 30, 40, 50]
# случайный элемент из списка
print(random.choice(number_list))
korzina = ['нан', 'май', 'сүт']
enumerateKorzina = enumerate(korzina)

print(type(enumerateKorzina))

# собираем в список
print(list(enumerateKorzina))

# изменяем
enumerateKorzina = enumerate(korzina, 5)
print(list(enumerateKorzina))

import random
 
number = random.randint(100, 1000)  
print(number)
#1
a = int(input())
b = int(input())
if a>b:
 print("Ошибка!")
else:
 print("все числа от A до B включительно")
for i in range(a, b + 1):
    print(i)
#2
a=int(input())
b=int(input())
 
if a<b:
    print("a<b выводим по возрастанию")                             
    for i in range(a, b+1):
        print(i)
else:
    print("b<a по убыванию")                               
    for i in reversed(range(b, a+1)):
        print(i)
#3
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')
#4
n = int(input())

s = 0
for i in range(n-1):
 s += int(input())

print("Потерянная карта {}".format((n+1)*n//2 - s))
#4/1
range_list = int(input("Сколько карточек у нас?   "))
num_remove = int(input("Какую карточку удалить?   "))
 
a = [int for int in range(1,range_list+1)]
a.pop(num_remove-1)
print(a)
 
x = sum(range(1,range_list+1))
y = sum(a)
z = x - y
 
print('Сумма диапазона: %d \nСумма значений: %d \nОтсутствует значение:  %d' % (x, y, z))

