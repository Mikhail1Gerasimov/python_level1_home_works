# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# Решение 
'''
Правила округления
Первое правило
Если первая из отделяемых цифр больше, чем число 5, то последняя из оставляемых цифр усиливается, иначе говоря, 
увеличивается на единицу. Усиление так же предполагается и тогда, когда первая из убираемых цифр равна 5, 
а за ней имеется одна или некоторое количество значащих цифр.

Второе правило
В случае если первая из отсекаемых цифр меньше чем 5, то усиления не производится.

Третье правило
Если отсекается цифра 5, а за ней не имеется значащих цифр, то округление выполняется на ближайшее четное число, 
другими словами, последняя оставляемая цифра остаётся неизменной, если она четная, и усиливается в случае, 
если она нечетная.

'''
def my_round(number, ndigits):
    num_str = str(number)
    if int(num_str[ndigits+2]) > 5:
        rounded = float(num_str[:ndigits+2])+float(1/int('1'+(int(ndigits)*'0')))
    elif int(num_str[ndigits+2]) == 5:
        if int(num_str[ndigits+3:]) > 0:
            rounded = float(num_str[:ndigits+2])+float(1/int('1'+(int(ndigits)*'0')))
        elif int(num_str[ndigits+2]) % 2 == 1:
            rounded = float(num_str[:ndigits+2])+float(1/int('1'+(int(ndigits)*'0')))
    else:
        rounded = float(num_str[:ndigits+2])
    
    if ndigits == 0:
        return int(rounded)
    else:
        return rounded
    

n,d=2.1234867,5
print(n,my_round(n, d),round(n, d))

n,d=2.1234567,5
print(n,my_round(n, d),round(n, d))

n,d=2.1999967,5
print(n,my_round(n, d),round(n, d))

n,d=2.9999967,5
print(n,my_round(n, d),round(n, d))

n,d=2.9999967,0
print(n,my_round(n, d),round(n, d))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

# Решение - не разобрался как НИЧЕГО print'ить
def lucky_ticket(ticket_number):
    num_str = str(ticket_number)
    left = 0
    right = 0
    for dig in num_str[:3]:
        left += int(dig)
    for dig in num_str[3:]:
        right += int(dig)
    if left == right:
        return 'lucky'
    else:
        return 'not_lucky'


a=lucky_ticket(123006)
b=lucky_ticket(436751)
c=lucky_ticket(12321)
print(a)
print(b)
print(c)