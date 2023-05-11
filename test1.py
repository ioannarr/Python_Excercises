# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverso(num):
    num = str(num)
    if num[0] == '-':  
        print(f'- ',{num[::1]})
    else:
        print(f'{num[::1]}')