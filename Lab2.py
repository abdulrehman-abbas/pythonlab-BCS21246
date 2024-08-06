count = 0
while (count < 5):
    print(count)
    count = count + 1

print("List Iteration")
list = ["hello", "world", "Newyork"]

for l in list:
    print(l)


'''iteration over string'''

testString = "hello"

for i in testString:
    print(i)


'''iteration by index'''

list = ["geeks", "for", "geeks"]

for i in range(len(list)):
    print(i)


''' Prints all letters except e and s'''

for letter in "greeksforgreeks":
    if letter == 'e' or letter == 's':
        continue
    print(letter, end="")

print("\n")


''' break the loop as soon as see e and s'''

for letter in "greeksforgreeks":
    if letter == 'e' or letter == 's':
        break
    print(letter, end="")
print("\n")


'''Functions'''
def myFunction():
    print("calling function")


myFunction()


print("\n")
'''Functions with parameters'''

def printName(fname):
    print("My name is ", fname)

printName("Abdulrehman")
printName("Abbas")


'''Default parameters in functions'''

def myCountry(country = "pakistan"):
    print("My country name is :", country)

myCountry()
myCountry("india")


'''passing list as parameter in functions'''

def printList(list):
    for l in list:
        print(l)

fruits = ["apple", "orange", "grapes"]
printList(fruits)


'''returning value'''

def doMath(num):
    return num * 3

print(doMath(10))


'''keyword parameters'''
def youngestChid(child1, child2, child3):
    print("The yougest child is :", child3)

youngestChid(child1="Abdulrehman", child2="Ali", child3="Farhan")

'''classes in python'''
class MyClass: x = 5

obj = MyClass()
print(obj.x)

'''class objects and methods'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getPerson(self): print("Name ", self.name, "Age ", self.age)

person1 = Person(name="Abdulrehman", age=10)
person1.getPerson()