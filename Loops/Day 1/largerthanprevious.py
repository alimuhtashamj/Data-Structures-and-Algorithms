num = [3, 5, 2, 4, 6, 1, 7]
count = 0 
for i in range(1,len(num)):
    if num[i] > num[i-1]:
        count += 1 
print(count)