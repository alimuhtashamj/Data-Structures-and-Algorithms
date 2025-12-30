# count increasing adjacent pairs
# if the second element is greater than the first, increase count

num = [3, 5, 2, 4]
count = 0 
for i in range(len(num)-1):
    # this range is selected because for 4, there is no adjacent increasing or decreasing 
    # number to compare with
   if num[i] < num[i+1]:
       count = +1
print(count)