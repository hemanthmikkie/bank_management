'''names=["Hemanth","Rohith","Sumanth","Vishnu",True,False,10,20.5]
print(names[0])
print(names[-1])
names[0]="Hemanth"
print(names[0]=="Hemanth") 
print("Hemanth" in names)'''

'''num=[1,2,3,4,5]
num.append(6) #insert at the end of the list
print(num)
num.extend([7,8,9]) #insert multiple values at the end of the list
print(num)'''



#count
'''num=[1,2,3,4,3,5,4,3,2,7,8,5,1,2,3]
#print(num.count(3)) #count the number of occurrences of a value in the list
#index
#print(num.index(2))#find the index of the first occurrence of a value in the list
num.pop() #remove the last element from the list
print(num)
num.pop(-2)
print(num)
num.pop(-6)
print(num)
num.clear() #remove all elements from the list
print(num)'''

'''num=[1,2,3,4,5,7]
num.insert(5,6) #insert a value at a specific index in the list
print(num)'''
#reverse
'''num=[3,2,1,5,4]
num.sort() #sort the list in ascending order
print(num)
num.sort(reverse=True) #sort the list in descending order
print(num)'''

'''num=[3,2,1,5,4]
num2=num.copy() #create a copy of the list
num.sort()
print(num)
print(num2)
print(id(num))
print(id(num2))'''

