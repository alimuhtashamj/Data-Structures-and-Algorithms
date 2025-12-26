# For every element, print the element and its next neighbor (use index-based thinking).
arr = [3, -2, 5, 1, -4, 5, 2]
for i in range(len(arr)-1):
    current = i 
    neighbor = i+1
    print(current, neighbor)
    