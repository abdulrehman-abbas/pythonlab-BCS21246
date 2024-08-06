def fabnochi_series(maxValue):
    series = [0,1]
    while True:
        next_value = series[-1] + series[-2]
        if (next_value > maxValue):
            break
        series.append(next_value)
    return series

print(fabnochi_series(50))