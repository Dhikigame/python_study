class MyException(Exception):
    pass

def div(a, b):
    try:
        if (b <= 0):
            raise MyException("not minus") #raise:故意に例外発生
        print(a / b)
    except MyException as e:
        print(e)
    else:
        print("no exception!")
    finally:
        print("-- end --")

div(10, -8.6)
# div(10, 3)
# div(10, 0)

