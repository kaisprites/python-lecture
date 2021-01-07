num_array = [3, 12, 45, 32, 54, 22]

num_sum = 0
num_max = num_array[0]
num_min = num_array[0]
for i in num_array:
    num_sum += i
    if num_max < i:
        num_max = i
    if num_min > i:
        num_min = i

print(num_array)
print(f"합계: {num_sum}")
print(f"평균: {num_sum/len(num_array)}")
print(f"최대값: {num_max}")
print(f"최소값: {num_min}")