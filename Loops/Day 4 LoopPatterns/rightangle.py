n = 5 
for i in range(5):
    # i = rows
    for j in range(i):
        # j = i means number of elements equivalent to no of rows(i) are being added
        # so for 2nd line, 2 asteriks are added and so on.
        print('*', end ='')
    # for a new line
    print()  