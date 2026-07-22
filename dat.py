


'''n=[1,2,3,4,5,6,7,8,9]
exist=False
for i in range(2,len(n)):
    if n[i]%n==0:
        print(" not prime num",n)
        exist=True
    else:
        print("prime num")'''



rows=5
n=1
for i in range(1,rows+1):
    res=" "
    for j in range(1,i+1):
        res+=str(n)+" " 
        n+=1
    print(res)



def fact(n):
     if n == 1:
        return 1
    return n*fact(n-1)
print(fact(5))
