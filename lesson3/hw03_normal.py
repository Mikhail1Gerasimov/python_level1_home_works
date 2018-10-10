# �������-1:
# �������� �������, ������������ ��� ��������� � n-�������� �� m-��������.
# ������� ���������� ���� ������� ����� 1 1
# �������
def fibonacci(n, m):
    fib = [1,1]
    for i in range(2,m,1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n-1:m+1]
print(fibonacci(4, 7))
print(fibonacci(1, 10))

# ������-2:
# �������� �������, ����������� ����������� ������ �� �����������.
# ��� ���������� ����������� ����� �������� (�������� �����������).
# ��� ������� ������ ������ ������ ������������ ���������� ������� � ����� sort()


def sort_to_max(origin_list):
    
    def min_finder(in_list):
        min_el = in_list[0]
        for el in in_list:
            if min_el > el:
                min_el = el
        return min_el
    
    sorted_list = []
    lst = origin_list
    while lst != []:
        sorted_list.append(min_finder(lst))
        lst.remove(min_finder(lst))
        
    return sorted_list
            

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# ������-3:
# �������� ����������� ���������� ����������� ������� filter.
# ����������, ������ ������ ������������ ���� ������� filter.
# �������
def filter_my_func(func,iterator):
    iterator_final = []
    
    for el in iterator:
        if func(el) == True:
            iterator_final.append(el)
    return iterator_final


def func(x):
    return x > 0
f1=func
print(filter_my_func(f1,[1,2,-1,-4,0,12]))

def func(x):
    return x**2 > 4
f2=func
print(filter_my_func(f2,[1,2,-1,-4,0,12]))

print(filter_my_func(lambda x: x**2 > 4,[1,2,-1,-4,0,12]))


# ������-4:
# ���� ������ ����� �1(�1, �1), �2(x2 ,�2), �3(x3 , �3), �4(�4, �4).
# ����������, ����� �� ��� ��������� ���������������.
# �������
'''
���� � ���������������� ��������������� ������� ������� �����, �� ���� ��������������� � ��������������. 
'''
A1 = (0,0)
A2 = (1,1)
A3 = (5,1)
A4 = (4,0)

def side_len_sq(cor1,cor2):
    return (cor1[0]-cor2[0])**2+(cor1[1]-cor2[1])**2

if side_len_sq(A1,A2) == side_len_sq(A3,A4) and side_len_sq(A2,A3) == side_len_sq(A4,A1):
    print('��������������')
elif side_len_sq(A1,A3) == side_len_sq(A2,A4) and side_len_sq(A2,A3) == side_len_sq(A4,A1):
    print('��������������')
else:
    print('�� ��������������')

