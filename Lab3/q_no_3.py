import random

random_num = random.randint(1,9)

result = int(input("Enter a number to guess between 1 to 9 "))
if(result == random_num):
   exit

while (result != random_num):
    result = int(input("Enter a number to guess between 1 to 9 "))
    
print("Well! Guessed")