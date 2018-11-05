class User:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print("{0}".format(self.name))

class AdminUser(User):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    def print_name(self):
        print ("{0} {1}".format(self.name, self.age))
