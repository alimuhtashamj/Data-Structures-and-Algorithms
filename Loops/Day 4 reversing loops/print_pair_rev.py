# print pairs where i < j in reverse order.
num = [1,2,3,4,5,6]
for i in range(len(num)-1,-1,-1):
    # i now has the highest index starting point satisfying i<j
    for j in range(i-1,-1,-1):
        # i-1 range satisfies the criteria of i < j index
        # if i's index is -1, j's will be -2(i-1)
        print(num[j], num[i])