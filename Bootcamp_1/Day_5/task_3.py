def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def is_in_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def even_odd_list_maker(list_q, func_1, func_2):
    list_of_odd = []
    list_of_even = []
    for i in list_q:
        if func_1(i):
            list_of_odd.append(i)
        elif func_2(i):
            list_of_even.append(i)
        
    return (list_of_odd, list_of_even)

a_list = range(1, 101)
odd, even = even_odd_list_maker(a_list, is_it_odd, is_in_even)

print("ODDS---- \n", odd)
print("EVENS---- \n", even)
            