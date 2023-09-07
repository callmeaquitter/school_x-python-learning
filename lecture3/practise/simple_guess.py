# ввод: любое натуральное число
# вывод: корень этого числа, если он целый
# если его нет - трудно, не могу
# def guess(num: int) -> int:

#81
#9

#80
#трудно

def guess(num: int) -> int:
    root = 0
    while root ** 2 <= num:
        if root ** 2 == num:
            return root
        root += 1
    return "Трудно, не могу"

num = int(input("Введите натуральное число: "))
result = guess(num)
print(result)