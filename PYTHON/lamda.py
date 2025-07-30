def new_func():

    a=float(input("enter the first number "))
    b=float(input("enter the second number "))
    c=float(input("enter the third number "))
    d=float(input("enter the forth number "))

    sum=lambda a,b,c,d:(a+b+c+d)
    substraction=lambda a,b,c,d:((a+b)-(c+d))
    multiplication=lambda a,b,c,d:(a*b*c*d)
    divition=lambda a,b,c,d:(a+b)/(c+d) if c+d !=0 else"not divisible by zero"
    avg=lambda a,b,c,d:((a+b+c+d)/4)
    total=lambda a,b,c,d:(a+b+c+d)
    percentage = lambda a, b, c, d: (a + b + c + d) *100/400

    print("sum is: ",sum(a,b,c,d))
    print("substraction is: ",substraction(a,b,c,d))
    print("multiplication is: ",multiplication(a,b,c,d))
    print("divition is : ",divition (a,b,c,d))
    print("avg is : ",avg (a,b,c,d))
    print("percentage is :", percentage (a,b,c,d))

new_func()


