#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def saco(array):
    for x in array:
        if 0 in array:
            array.remove(0)
            array.append(0)
    return array