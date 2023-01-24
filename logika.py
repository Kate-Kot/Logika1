import random

lista = list(range(1, 11))
listb = list(range(1, 11))
def chet():
    random.shuffle(lista)
    random.shuffle(listb)
    print(lista, len(lista))
    print(listb, len(listb))
    k = 0
    while k < 10 :
        b = listb[k]
        k +=1
        for a in lista:
            ot = input(f'Подскажи, сколько будет {a} * {b} ?')
            if ot.isdigit():
                otvet = int(ot)
            else:
                otvet = 0

            resh = a*b
            if otvet == resh:
                    print('Ура! Правильно! Ты молодец!!!\n')
            else:
                    print(f'Мне жаль, но тут ошибка. {a} * {b} = {resh}\n')

chet()
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)