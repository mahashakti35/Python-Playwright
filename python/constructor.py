class MyClass:
    def __init__(self,a,b):
        self.firstNum = a
        self.secondNum = b
        print("This is constructor")
    def method(self):
        print("This is method")
    def cal(self):
        return self.firstNum +self.secondNum
# obj = MyClass(2,3)
# obj.method()
obj2 = MyClass(5,6)
print(obj2.cal())