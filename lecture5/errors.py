def conver_ab_to_int(a: str, b:str) -> tuple[int, int]:
    a, b = int(a), int(b)
    return a, b
def divide_ab (a: int | float, b: int | float) -> float
    return a / b
while True:
    a, b = input('Введите два числа для их суммы:').split()
    try:
        a, b, = conver_ab_to_int(a, b)
        division_scope = divide_ab(a, b)
    except ZeroDivisionError as e:
        print(f'Произошла ошибка: {e}')
        print('Давай без нулей')
        print()
        continue

    ad_sum = a + b
    print(f'Сумма {a} + {b} = {ad_sum}')
    print(f'{a} / {b} = {division_scope}')
    print