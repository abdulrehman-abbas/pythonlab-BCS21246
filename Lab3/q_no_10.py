# range of no 1-50 print Fizz if multiple of 3 Buzz if multiple of 5 and FizzBuzz if is divisble of both 3and 5
for i in range(1,51):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
