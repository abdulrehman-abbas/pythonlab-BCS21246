# no of even and odd

nums = [1,2,3,4,5,6,7,8,9]

even_count = 0
odd_count = 0
for i in nums:
    if(i % 2 == 0):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Number of evens are :", even_count)
print("Number of odds are :", odd_count)
