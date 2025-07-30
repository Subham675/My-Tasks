# n = int(input("Enter the value for n: "))
# k = 1
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(k, end=" ")
#         k += 1
#     print()



number=int(input('enter a number'))
factorial=1
if number<0:
    print("factorial does not exist for negetive numbers")
elif number == 0:
    print("the factorial of 0 is 1")
else :
    for i in range(1,number+1):
        factorial = factorial*i
# print(f"the factorial of number {number} is {factorial}")