'''def pora(name):
    #return "Hello, " + name
    print("Hello, " + name)
print(pora("Hemanth"))'''

'''def a(a,b=80):
    return a+b
print(a(10))'''

'''words="pythoon"
s=""
for i in range(len(words)):
    if words[i].lower()==words[i]:
        s+=words[i].upper()
    else:
        s+=words[i].lower()
print(s)'''


'''words="book"
char="o"
pos=2
s=""
count=0
for i in range(len(words)):
    if words[i]==char:
        count+=1
    if count==pos:
        s+=words[i].upper()
    else:
        s+=words[i]
print(s)'''



'''words="ASDDFGHyuodfgk"
s=""
for i in range(len(words)):
    if i>2== 0:
        s+=words[i].upper()
    else:
        s+=words[i].lower()
print(s)'''

'''user="Hemanth"
inp_user=input("Enter your name: ")
print(user==inp_user.strip())'''


'''words="       black pen     "
s=""
for i in range(len(words)):
    if words[i]!=" ":
        s+=words[i]
print(s)'''


'''print("            Green pen        ".rstrip())

print("            Green pen        ".lstrip())

print("            Green pen        ".strip())'''
'''words="black pen"
word=words.split()
for i in range(len(word)):
    print(word[i][::-1],end=" ")'''
sentence="hell0 world"
words=sentence.split(" ")
for word in range(len(words)):
    rev="" 
    for i in range(len(words[word])-1,-1,-1):
        rev=words[word][i]+rev
print(rev,end=" ")
