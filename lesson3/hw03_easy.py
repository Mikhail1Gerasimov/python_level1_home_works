# �������-1:
# �������� �������, ����������� ���������� ������������ ���������� �����
# �� ���-�� ������ (���-�� ������ ���������� ������ ����������).
# ���������� ������ ����������� �� �������������� �������� (0.6 --> 1, 0.4 --> 0).
# ��� ������� ������ �� ����������� ���������� ������� � ������� �� ������ math.
# ������� 
'''
������� ����������
������ �������
���� ������ �� ���������� ���� ������, ��� ����� 5, �� ��������� �� ����������� ���� �����������, ����� ������, 
������������� �� �������. �������� ��� �� �������������� � �����, ����� ������ �� ��������� ���� ����� 5, 
� �� ��� ������� ���� ��� ��������� ���������� �������� ����.

������ �������
� ������ ���� ������ �� ���������� ���� ������ ��� 5, �� �������� �� ������������.

������ �������
���� ���������� ����� 5, � �� ��� �� ������� �������� ����, �� ���������� ����������� �� ��������� ������ �����, 
������� �������, ��������� ����������� ����� ������� ����������, ���� ��� ������, � ����������� � ������, 
���� ��� ��������.

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


# �������-2:
# ��� ������������ ����� ������. ����������, �������� �� ����� ����������.
# ������� ����������� � ���� �������.
# ����� ��������� ����������, ���� ����� ��� ������ � ��������� ���� �����.
# !!!P.S.: ������� �� ������ ������ print'���

# ������� - �� ���������� ��� ������ print'���
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