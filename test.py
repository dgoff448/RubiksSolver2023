def swapSlices(arr, a, b, c, d):
    if a < c and b < d:
        s1 = arr[0:a]
        s2 = arr[a:b]
        s3 = arr[b:c]
        s4 = arr[c:d]
        s5 = arr[d:len(arr)]
    else:
        s1 = arr[0:c]
        s2 = arr[c:d]
        s3 = arr[d:a]
        s4 = arr[a:b]
        s5 = arr[b:len(arr)]

    print(s1, s2, s3, s4, s5)
    return  s1 + s4 + s3 + s2 + s5


def push(arr, a, b, c, d):
    if a < c and b < d:
        s1 = arr[0:a]
        s2 = arr[a:b]
        s3 = arr[b:c]
        s4 = arr[c:d]
        s5 = arr[d:len(arr)]

        print(s1, s2, s3, s4, s5)
        return [s1 + [-1]*len(s2) + s3 + s2 + s5, s4]
    else:
        s1 = arr[0:c]
        s2 = arr[c:d]
        s3 = arr[d:a]
        s4 = arr[a:b]
        s5 = arr[b:len(arr)]

        print(s1, s2, s3, s4, s5)
        return [s1 + s4 + s3 + [-1]*len(s4) + s5, s2]

    
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr)
print(swapSlices(arr, 0, 1, 9, 10))
print()
print(arr)
print(swapSlices(arr, 9, 10, 0, 1))

# print(push(arr, 1,3,6,8))
# print()
# print(push(arr, 6,8,1,3))