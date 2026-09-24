arr  = [3,6,5,6,7,8,9,10]

n = len(arr)

def gun():
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(gun())

# o(n)
# o(1) 