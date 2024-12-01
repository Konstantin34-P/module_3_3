def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(1, 2, 3)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [11, 'cool', False]
print_params(*values_list)
values_dict ={'a' : 10, 'b': 20, 'c' : 30}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)