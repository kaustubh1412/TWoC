  
number = int(input("Enter range: "))

a = 0
b = 1
count = 0

    print("Fibonacci series upto ",number)
    while count < number:
        print(a)
        num_new = a + b
        a = b
        b = num_new
        count += 1
