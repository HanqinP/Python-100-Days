from math import sqrt

num = int(input("input a number:"))
sqrtn = int(sqrt(num))
prime_flag = True

print(f"number is {num}, sqrt of number is {sqrtn}")

for i in range(2, sqrtn+1):
    if num % i ==0:
        print("This number is not prime number")
        prime_flag = False
        break

if prime_flag and num != 1:
    print(f"The number {num} is prime number")