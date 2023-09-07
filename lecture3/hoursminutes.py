num: int = int(input("Введите число в сек: "))
minute = num // 60
if minute < 60:
    print(f"0 час(ов) и {minute} минут(а/ы)")
else:
    hours1 = num // 60
    hours2 = hours1 // 60
    minutes = hours1 - hours2 * 60    
    print(f" {hours2} час(ов) и {minutes} минут(а/ы)")


#prettier

num = int(input("Введите число в сек: "))


hours1 = num // 60
hours2 = hours1 // 60
minutes = hours1 - hours2 * 60  

if hours2 == 1:
    timehours = "1 час"
elif hours2 in [2, 3, 4]:
    timehours = f"{hours2} часа"
else:
    timehours = f"{hours2} часов"

if minutes == 1:
    timeminutes = "1 минута"
elif minutes in [2, 3, 4]:
    timeminutes = f"{minutes} минуты"
else:
    timeminutes = f"{minutes} минут"

print(f"{timehours} и {timeminutes}")

