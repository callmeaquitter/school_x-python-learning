num: int = int(input("Введите число в сек: "))
minute = num // 60
if minute < 60:
    print(f"0 час(ов) и {minute} минут(а/ы)")
else:
    hours1 = num // 60
    hours2 = hours1 // 60
    minutes = hours1 - hours2 * 60    
    print(f" {hours2} час(ов) и {minutes} минут(а/ы)")