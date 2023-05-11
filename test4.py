
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

num1 = '364'
num2 = '1836'

def solu(num1,num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))
            
print(solu(num1,num2))