def heart(n):
    for i in range (n//2,n+1,2):
        print(" "*((n-i)//2),end="")
        print("*",end=" ")
        print(" "*(n-i),end="")
        print("*"*i)
    for i in range(n,0,-1):
        print(" "*(n-i),end="")
        print("*"*(2*i-1))
n=6
heart(n)