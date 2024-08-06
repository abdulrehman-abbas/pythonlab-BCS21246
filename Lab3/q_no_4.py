'''
program to print this pattern

*
**
***
****
*****
****
***
**
*
'''


def printPattern():
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")

        print("\n")
    for i in range(4, 0, -1):
        for j in range(i):
            print("*", end="")
        print("\n")

printPattern()