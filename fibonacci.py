a=0
b=1
n=int(input("\nenter a no: "))
print(a,b,end=' ')
for i in range(n):
    c=a+b
    a=b
    b=c
    if(c<n):
        
         print(c,end=' ')
