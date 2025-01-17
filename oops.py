### 1. Demo Class
class Demo:
    value = 0

    def __init__(self, val1, val2):
        self.instance_var1 = val1
        self.instance_var2 = val2

    def Fun(self):
        print(f"Fun Method: Instance Var1 = {self.instance_var1}, Instance Var2 = {self.instance_var2}")

    def Gun(self):
        print(f"Gun Method: Instance Var1 = {self.instance_var1}, Instance Var2 = {self.instance_var2}")


Obj1 = Demo(11, 21)
Obj2 = Demo(51, 101)

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()



### 2. BookStore Class
class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.Name} by {self.Author}. No of books: {BookStore.NoOfBooks}")


Obj1 = BookStore("Linux System Programming", "Robert Love")
Obj1.Display()

Obj2 = BookStore("C Programming", "Dennis Ritchie")
Obj2.Display()



### 3. Circle Class
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter radius: "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print(f"Radius: {self.Radius}, Area: {self.Area}, Circumference: {self.Circumference}")


circle1 = Circle()
circle1.Accept()
circle1.CalculateArea()
circle1.CalculateCircumference()
circle1.Display()



### 4. BankAccount Class

class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Deposit(self):
        deposit_amount = float(input("Enter amount to deposit: "))
        self.Amount += deposit_amount

    def Withdraw(self):
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount <= self.Amount:
            self.Amount -= withdraw_amount
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest: {interest}")

    def Display(self):
        print(f"Name: {self.Name}, Amount: {self.Amount}")


account1 = BankAccount("John Doe", 1000)
account1.Deposit()
account1.Withdraw()
account1.CalculateInterest()
account1.Display()


### 5. Numbers Class

class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        return sum(i for i in range(1, self.Value) if self.Value % i == 0)


num = Numbers(28)
print("Is Prime:", num.ChkPrime())
print("Is Perfect:", num.ChkPerfect())
print("Factors:", end=" ")
num.Factors()



### 6. Numbers Class (Arithmetic Operations)

class Numbers:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = float(input("Enter Value1: "))
        self.Value2 = float(input("Enter Value2: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Division by zero not allowed"


num = Numbers()
num.Accept()
print("Addition:", num.Addition())
print("Subtraction:", num.Subtraction())
print("Multiplication:", num.Multiplication())
print("Division:", num.Division())

