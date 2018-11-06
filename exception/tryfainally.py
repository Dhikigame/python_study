try:
    a = 10 / 1
#    a = 10 / 1
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("ZeroDivisionError!!")
else:
    print("else statement") # else:エラー起こらず進めば発生
finally:
    print("finally statement") # fainally:必ず最後に発生