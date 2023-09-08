alphabet = {
    0: 'AA',
    1: "A",
    2: "B",
    3: "C",
    4: "X",
    10: "Y",
    'Z': 10,
    1.1: '12',
    0.1: 'SDA',
    True: 'sdasd',
    False: 123123,
    None: 'dasdasd',
    [1,2]: 3,
}


class A:
     def __init__(self, **kwargs):
        for key, valeu in kwargs:
            
                        


# o_letter = (alphabet.get('Z', None))
# if not o_letter:
#         print('NO O')


for key, value in alphabet.items(): # .keys() .values()
        print(f"Ключ: {key} Значение {value}")