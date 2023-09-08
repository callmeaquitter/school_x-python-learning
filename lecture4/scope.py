z = 12

def outer():
    # print("y in outer befor assig: {"y" in locals()}")
    y = 12
    def answer ():
        return x
    return answer()

if __name__ == "__main__":
    x = 42
    print(
        "y" in locals()
    )