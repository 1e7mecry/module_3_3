def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(2, 3)
values_list = [12, 'python', False]
values_dict = {'a': 13, 'b': [1, 2], 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list2 = ['number', (3, 5)]
print_params(*values_list2,  42)

