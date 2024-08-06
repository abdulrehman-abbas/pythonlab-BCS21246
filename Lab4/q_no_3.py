def binarySearch(array, number):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        if array[mid] > number:
            high = mid - 1
        elif array[mid] < number:
            low = mid + 1
        else:
          return mid; 
    
    return -1


data = [1,3,55,67,88,99,855,1123,2225]

result = binarySearch(data, 99)
if result != -1:
 print("Element found")
else:
 print("Not found")
