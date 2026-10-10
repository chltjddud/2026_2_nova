numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(numbers)
