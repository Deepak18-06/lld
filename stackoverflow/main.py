def test1():
    pass
def test2():
    pass
if __name__ == "__main__":
    try:
        print("--------------Test 1 ------------------")
        test1()
        print("------------- Test2 -------------------")
        test2()
    except Exception as e:
        print(e)