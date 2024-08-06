def generate2dArray(m, n):
    array = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(i * j)
        array.append(row)
    return array


rows = int(input("Enter no of rows :"))
columns = int(input("Enter no of columns :"))

result = generate2dArray(rows, columns)

for row in result:
    print(row)