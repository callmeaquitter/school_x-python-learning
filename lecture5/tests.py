a: list[int] = [1, 2, 3, 3, 5]
b: list[int] = [0, 0, 1 ,0, 1]
#     answer = [0, 0, 3, 0, 5] 

def mask_list(array: list[int], mask: list[int] ) -> list[int]:
    return [val * b[i] * .5 for i, val in enumerate(array)]

def test_mask_list():
    print('Проверяем тест маск лист')
    assert mask_list([1, 2, 3], [0, 1, 0]) == [0, 2, 0]

answer = mask_list(array = a, mask = b)

# answer_1 = [
#     val*b[i]
#     for i, val in enumerate(a)] #1 variant
# print(answer_1)












# answer_2 = []
# for i, val in enumerate(a):
#     answer_2.append(val * b[i]) #2 variant
# print(answer_2)

# for i, val in enumerate(a):
#     print