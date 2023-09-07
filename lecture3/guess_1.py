# def my_personal_sum(
#         x:int | float,
#         y:int | float,
# )  ->    int | float: 
#     return x + y
# print(my_personal_sum(3, 5))

def my_personal_sum(*args, **kwargs) -> int | float:
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

print(my_personal_sum(3, 5, 1, 5, name="bob"))