import math

def is_prime_num (num):
    val = 2
    if num < 2:
        return "Not Prime"
    while val < num:
        if num % val != 0:
            return "Prime"
        else :
            return "Not Prime"
        val +=1
    # OR
    '''
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
        else:
            return "Prime"
    '''
    
    
number = int(input("Enter a number : "))

print(is_prime_num(num=number))