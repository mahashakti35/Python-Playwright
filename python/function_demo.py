def greetMe(name):
    print("Hello "+name)
greetMe("Sonu")

class Calculator:
    num1 = 100
    num2 = 200
    def add(self):
        print("add")
obj = Calculator()
print(obj.num1+obj.num2)
obj.add