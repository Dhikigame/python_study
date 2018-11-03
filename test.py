class User:
    count = 0
    def __init__(self, name):
        User.count += 1
        self.__name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.__name))
    # クラスメソッド
    @classmethod
    def show_info(cls):
        print("{0} instances".format(cls.count))

tom = User("tom")
bob = User("bob")

print(tom.__name)
bob.say_hi()

#User.show_info()
#tom.show_info()