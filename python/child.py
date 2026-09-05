from constructor import MyClass


class Child(MyClass):
    num2 = 200
    def __init__(self):
        MyClass.__init__(self,10,20)
    def method(self):
        return self.num2 + self.cal()
obj = Child()
print(obj.method())