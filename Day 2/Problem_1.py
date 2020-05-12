
def even_odd_check(number):
    if number%2==0:
        return True
    else:
        return False

def prime_check(number):
    a = 2
    k = number//2
    while k>=a:
        if number%a==0:
            return False
        a+=1
        k=number//a
    return True

def pallindrome_check(number):
    number = str(number)
    length = len(number)
    for i in range(length//2):
        if number[i]!=number[length-1-i]:
            return False
        return True

def armstrong_check(number):
    sum = 0
    temp = number
    while temp>0:
        digit = temp%10
        sum+= digit**3
        temp//=10
    if number==sum:
        return True
    return False


def check():
    number = int(input("Enter a number: "))
    if(even_odd_check(number)):
        print(number, " is odd")
    else:
        print(number, " is even")
    if(prime_check(number)):
        print(number, " is prime")
    if(pallindrome_check(ṇumber)):
        print(number, " is pallindrome")
    if(armstrong_check(number)):
        print(number, " is armstrong")




    
        