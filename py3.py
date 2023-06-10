def input_val_fac(num):
    

    fac =1
    for i in range(1,num+1):
        fac = fac * i
    return fac

def count_zero_in_fac(n):
    count = 0

    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5

    return count




num = int(input("Input your number factorial : "))
factorial_val = input_val_fac(num)
print(f"Factorial of {num} is : ",factorial_val)    

num_zero = count_zero_in_fac(num)
print("Count of zero : ",(num_zero))
