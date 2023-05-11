
# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

newA = A.sort()
print(newA)
for x in range(0, len(newA)-1):
    if all(newA[x]>= newA[x+1]):
        print ('True')
    else:
        print ('False')

newB = B.sort()
print(newB)

newC = C.sort()
print(newC)
