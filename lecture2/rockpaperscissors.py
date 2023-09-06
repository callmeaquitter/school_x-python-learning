ftplayer, scplayer = input("Введите два слова, разделённые пробелами: ").split()

rules = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}

if ftplayer == scplayer:
    print("Ничья!")
elif rules[ftplayer] == scplayer:
    print("Игрок 1 выиграл!")
else:
    print("Игрок 2 выиграл!")
