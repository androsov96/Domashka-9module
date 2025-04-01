list_int = [6, 20, 15, 9]
list_str = ['Anton', 'Vlad', 'Olga', 'Anna', 'Aleksandr']

def apply_all_func(_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(_list)
    return results

print(apply_all_func(list_int, max, min))
print(apply_all_func(list_int, len, sum, sorted))

print(apply_all_func(list_str, max, min))
print(apply_all_func(list_str, len, sorted))