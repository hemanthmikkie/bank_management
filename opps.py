# class car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         print("Car created automatically")
# # bwm=car("BMW", "X5", 2020)
# # print(bwm.brand)
# # print(bwm.model)


# trumiph=car("trimuph","tiger",2025)
# print(trumiph.brand)


# class stu:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def paly(self):
#         print("hello",self.name)
#         print("your age",self.age)
# p=stu("hemanth",20)
# p1=stu("Alice",21)
# p.paly()
# p1.paly()





# class mob:
#     calling = True
#     def make_call(self):
#         return " it's make call function"
# class smartmob(mob):
#     intertnet = True
#     def mak_cal(self):
#         return " it's acces internet"


# landline=mob()
# print(landline.calling)
# print(landline.make_call())




# x7pro=smartmob()
# print(x7pro.calling)
# print(x7pro.make_call())



#encapsulation

# class sbi:
#     bank_name="sbi"
#     bank_acc=["savings","current","fixed","joint"]
#     def main_branch(self):
#         return " welcome to sbi main bramnch"
#     def applicatin(self):
#         return " go to the next counter fr application"
# class kkl_sbi(sbi):
#     def __init__(self):
#         self.cheque_deoposit = True
#     def cheque_withdraw(self):
#         return " thank you for withdraw and have a nice day"



# hemanth=kkl_sbi()
# # print(hemanth.cheque_deoposit)
# # print(hemanth.cheque_withdraw())


# print(hemanth.bank_name)
# print(hemanth.bank_acc)
# print(hemanth.main_branch())

# # hemanth=kkl_sbi()
# print(hemanth.cheque_deoposit)
# print(hemanth.cheque_withdraw())




#multiple inheritance
# class father():
#     give_monney=True
# class mother():
#     caring=True
# class child(father,mother):
#     def __init__(self,name):
#         self.name=name
# child1=child("minnie")
# print(child1.name)
# print(child1.give_monney)




#multilevel inheritance
# class animal():
#     def sound1(self):
#         return " make a sound"
# class dog(animal):
#     def sound2(self):
#         return " bark"
# class puppy(dog):
#     def sound3(self):
#         return " bark like a puppy"
# class name(puppy):
#     pass
# s=puppy()
# print(s.sound3())




#heirarchical inheritance
# class vechile():
#     def wheels(self):
#         print("vechile strated")
# class car(vechile):
#     def wheels(self):
#         print("car strated")
# class bike(vechile):
#     def wheels(self):
#         print("bike strated")
# c=car()
# b=bike()
# c.wheels()
# b.wheels()

# class a:
#     def __init__(self):
#         print("class a constructor")
# class b(a):
#     def __init__(self):
#         print("class a constructorrrr")
# b()










#n
# class bank:
#     def __init__(self, name, acc_no, balance, password):
#         self.name = name
#         self.acc_no = acc_no
#         self.balance = balance
#         self.__password = password

#     def show_password(self):
#         print(self.__password)

#     def set_password(self, password):
#         self.__password = password

# a = bank("hemanth", 123456789, 10000, "uhuv")
# print(a.name)
# print(a.acc_no)
# # print(a.balance)

# a.set_password("mynew")
# a.show_password()

# Do not access or call the private attribute directly:
# a.__password("mynew")
# print(a.__password)

# Directly assigning to the mangled private attribute is not recommended:
# a.__password = "mynew"
# a.show_password()

#polymoripsim
#methdn bahevingndifrently in diffrent class
#complie time pilymorphism
#run the polymorphisim











#abstrction-> hiding th eimplemtation details and show the esstinal featuress

# from abc import ABC,abstractmethod
# class vechile():
#     def engine(self):
#         pass
#     def car(self):
#         pass
# c = vechile()
# print(c)





# from abc import ABC,abstractmethod
# class vechile(ABC):
#     @abstractmethod
#     def engine(self):
#         pass
# class car(vechile):
#     def engine(self):
#         return "its petro car"
# class train(vechile):
#     def engine(self):
#         return super().engine()
#     # pass
    
    
# c = car()
# t=train()








class studet():
    def __init__(self,roll_num,name,num):
        self.roll_num=roll_num
        self.name=name
        self.num=num
    def purpose(self):
        return " to attended the college"
# data=studet(2213139,"hemanth",9642651775)
# print(data.name)
# print(data.roll_num)




#super-> to access parent class methods and properties from child class



class stu(studet):
    def __init__(self,roll_num,name,num):
        super().__init__(roll_num,name,name)
    def pupose(self):
        return super().purpose()
data=studet(2213139,"hemanth",9642651775)
print(data.name)
print(data.roll_num)
print(studet.purpose)


