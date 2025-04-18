def is_prime(func):
    def wrapper(*args):
        result_func = int(func(*args))
        set_prime = None
        if result_func == 0 or result_func == 1:
            set_prime = 'Не простое не составное'
        for i in range(2, result_func + 1):
            if result_func % i == 0:
                set_prime = 'Составное'
                break
            else:
                set_prime = 'Простое'
        print(set_prime)
        return result_func

    return wrapper


@is_prime
def sum_three(a, b, c):
    result_ = a + b + c
    return result_


result = sum_three(3, 3, 6)
print(result)
print(sum_three(0, 0, 0))
print(sum_three(1, 0, 0))
print(sum_three(2, 3, 6))
print(sum_three(3, 3, 9))
