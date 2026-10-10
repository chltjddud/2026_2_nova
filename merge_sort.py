numbers = [64, 34, 25, 12, 22, 11, 90]
n = len(numbers)

width = 1
while width < n:
    for i in range(0, n, 2 * width):
        left = numbers[i : i + width]
        right = numbers[i + width : i + 2 * width]
        
        merged = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        merged.extend(left[l:])
        merged.extend(right[r:])
        
        numbers[i : i + len(merged)] = merged
    width *= 2

print(numbers)
