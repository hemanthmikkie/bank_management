'''rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        res+="* "  
    print(res)'''

'''rows=int(input("enter the number of rows"))
for i in range(1,rows+1):
    res=" "
    for j in range(1,i+1):
        res+=str(rows)+" "  
    print(res)'''


'''rows=int(input("enter the number of rows"))
for i in range(1,rows+1):
    res=" "
    for j in range(rows-i+1):
        res+="*"+" "  
    print(res)'''


'''rows=int(input("enter the number of rows"))
for row in range(1,rows+1):
    res=" "
    for col in range(1,rows+1):
        if row==1 or row==rows or col==1 or col==rows:
            res+="* "
        else:
            res+=" "+" "
    print(res)'''


'''rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        if i==1 or i+j==rows+1:
            res+="*"+" "
    else:
        res+="  "
    print(res)'''

5
'''rows=int(input("enter the no of rows"))
for i in range(1,rows+1):
    res=""
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(rows-1,0,-1):
    res=""
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)'''


'''rows=int(input("enter the no of rows"))
for i in range(rows,0,-1):
    res=""
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)
for i in range(2,rows+1):
    res=""
    for sp in range(1,rows-i+1):
        res+=" "
    for j in range(1,i+1):
        res+="*"+" "
    print(res)'''


'''rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,i+1):
        res+=str(i*j)+" "
    print(res)'''



rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if (i+j)%2==0:
            res+="x "
        else:
            res+="o "
    print(res)