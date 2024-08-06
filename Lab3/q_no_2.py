# celsius to farenhite and farheite to celsius

def farenhite_to_celsius(farenhite):
    result =(5/9) * (farenhite - 32)
    return result


def celsius_to_farenhite(ceslius):
    result = ((9/5) * ceslius) + 32
    return result

print(format(farenhite_to_celsius(45), '.2f'))
print(format(celsius_to_farenhite(7), '.2f'))