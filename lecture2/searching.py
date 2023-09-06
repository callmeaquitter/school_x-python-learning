lst = list(map(int, input().split()))
spisok = []
for i in range(1, len(lst)):
    if lst[i] - lst[i-1] > 1:
        spisok.append(i)
if not spisok:
    print("Не найдено")
elif len(spisok) == 1:
    print(spisok[0])
else:
    print(spisok)