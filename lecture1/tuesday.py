# print ("В итоге получилось: {}, {}".format(answer, first))
# print(f"В итоге получилось: {a}")
N = int(input("Введите число: "))
sum_3 = 3 * ((N // 3) * ((N // 3) + 1) // 2)
sum_5 = 5 * ((N // 5) * ((N // 5) + 1) // 2)
sum_15 = 15 * ((N // 15) * ((N // 15) + 1) // 2)
sum = sum_3 + sum_5 - sum_15
print(sum)