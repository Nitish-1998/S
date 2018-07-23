#age = int(input('Enter your age:'))
#if age<5:
 #  print('no ticket')
#elif age>5 and age<12:
 #  print('50% discount')
#elif age>12 and age<60:
 #  print('10% discount')
#else:
 #  print('60% discount')
#num1=int(input('Enter first number:'))
#num2=int(input('Enter second number:'))
#if num1>num2:
 #  print('first number is Maximum',num1)
#else:
  # print('second number is maximum',num2)
#a,b,c=10,20,25
#if a>b and a>c:
 #  print('a is max',a)
#elif b>a and b>c:
 #  print('b is max',b)
#else:
   #print('c is max',c)
#a=[10,20,50,80,1,5,7,90,295,25]
#greatest=a[0]
#for i in range(0,len(a)-1):
#        greatest=a[i]
#    else:
#        i=i+1
#print('greatest',greatest)


#a=int(input('Enter any number:'))
#if a%5==0 and a%11==0:
 #  print('it is divisible by 5 and 11 both')
#elif a%11==0:
  # print('it is divisible by 11')
#else:
 #  print('if is not divisible by both')


#alp=input('Enter any character:')
#if alp=='a' or alp=='e' or alp=='i' or alp=='o' or alp=='u'or alp=='A' or alp=='E' or alp=='I' or alp=='O' or alp=='U':
#    print('It is a vowel')
#else:
#    print('It is a consonent')


#phy=int(input('Enter physics number:'))
#chm=int(input('Enter chemistry number:'))
#bio=int(input('Enetr biology number:'))
#mat=int(input('Enter maths number:'))
#com=int(input('Enter computer number:'))
#t= phy+ chm+ bio+ mat+ com
#per=t/500*100
#print("Percntage= ",per)
#if per>=90 and per<=100:
#    print('A')
#elif per>=50 and per<=90:
#    print('B')
#elif per>=70 and per<=80:
#    print('C')
#elif per>=50 and per<=70:
#    print('D')
#elif per>=33 and per<=50:
#    print('E')
#elif per<=33:
#    print('F')
#else:
#    print('F')
#def add (a,b):
#     c=a+b
     #return c
#a= int(input('Enter a no:'))
#b= int(input('Enter second no:'))
#c= add(a,b)
#print(c)
#def avg (a,b):
#    c=(a+b)/2
#    return c
#n1=int(input('Enter 1st no.:'))
#n2=int(input('Enter 2nd no.:'))
#res= avg(n1,n2)
#print(res)

#def Max (a,b):
#    if a>b:
#        return a
#    else:
#        return b
#n1=int(input('Enter 1st no.:'))
#n2=int(input('Enter 2nd no.:'))
#res= Max(n1,n2)
#print(res)


#def max(a,b,c):
#    if a>b and a>c:
#        return a
#    elif b>a and b>c:
#        return b
#    else:
#        return c
#a = int(input('Enter first number:'))
#b = int(input('Enter second number:'))
#c = int(input('Enter third number:'))
#d = max(a,b,c)
#print('Maximum number is:',d)

#========Small Example=========================
#def sumall(l):
#    sum=0
#    for ele in a:
#        sum = sum + ele
#    return sum
#a =[10,20,30,40,50,60,70,80,90]
#print(sumall(a))

#========Even Example==========================
#def evn(l):
#    for i in range(0,len(l)-1):
#        if l[i]%2==0:
#            print(l[i])
#        else:
#            i=i+1
#l=[2,3,4,5,6,7,8,9]
#evn(l)
#========Hello while===========================
#for i in range(0,10):
#    print(i+1,'Hello')
#========Swap number Example===================
#i=0
#while i<10:
#    i=i+1
#def swap(a,b):
#    c=0;
#    c=a
#    a=b
#    b=c
#    print(a,b)
#a=int(input('Enter a :'))
#b=int(input('Enter b :'))
#swap(a,b)
#====== Append Example ==========================
#a = [10, 20, 30]
#a.append(50)
#print(a)
#======= Inser Example ==========================
#a = [10, 20, 30 ]
#a.insert(1,25)
#print(a)
#======== Append Example ========================
#a = [10, 20, 30]
#a.append('Ram')
#print(a)
#======== List access Example ==================
#a = [10, 20, 30, [1, 2, ['A', 'B']]]
#print(a[3][1])
#print(a[3][2][1])

#============ Insert Example ==================#
#a = [10, 20, 30 ]
#a.insert(1,40)
#print(a)
#a.insert(3,'Ram')
#print(a)
##============ Dictonary examples with lists ================#
#my_list = []
#my_dict_1 = { 'name' : 'abs',

#              'roll' : 123
#            }
#my_dict_2= { 'name' : 'abx',
#             'roll' : 1234
#           }
#my_dict_3 = { 'name' : 'absas',
#              'roll' : 1235
#            }
#my_list.append(my_dict_1)
#my_list.append(my_dict_2)
#my_list.append(my_dict_3)
#print(my_list[1]['name'],my_list[1]['roll'] )
#print(my_list)
##============= Slicing Example =================================

#a=[1,2,3,4,5,6,7,8,9]
#print(a[1:4])

#a = ['cat' , 'dog' , 'rat' , 'bird' , 'hen']
#print(a[:3])
#print(a[3:])
#print(a[2:3])

#a = 'India'
#print(a[1:3])
#print(a[2:])
#print(a[:4])
#print(a[:])

#================= Class Example ================================
##1
#class student:
#    def __init__(self,name,age,year):
#        self.name = name
#        self.age = age
#        self.year = year
#    def get_name(self):
#

#    def get_age(self):
#        print(self.age)
#
#    def change_year(self):
#        self.year = self.year + 1
#s1 = student('Roy' , 20 , 1)
#s1.get_name()
#s1.get_age()
#print(s1.year)
#s1.change_year()
#print(s1.year)

#s2 = student('Ram' , 22 , 4)
#s2.get_name()
#s1.get_name()
#s2.get_age()
#print(s2.year)
#s2.change_year()
#print(s2.year)

##2

#class student:
#    branch = 'cse'                                                              #Class member
#    def __init__(self,name,age,year):                                           #Constructer
#        self.name = name                                                        #Object member
#        self.age = age
#        self.year = year
#    def get_name(self):
#        print(self.name)
#
#    def get_age(self):
#        print(self.age)
#
#    def change_year(self):
#        self.year = self.year + 1
#s1 = student('Roy' , 20 , 1)
#s1.get_name()
#s1.get_age()
#print(s1.year)
#s1.change_year()
#print(s1.year)

#s2 = student('Ram' , 22 , 4)
#s2.get_name()
#s1.get_name()
#s2.get_age()
#print(s2.year)
#s2.change_year()
#print(s2.year)
#print(s1.branch)
#print(s2.branch)
#s1.branch = 'Mech'
#print(s2.branch)
#s2.branch = 'Civil'
#print(s1.branch)
#print(s2.branch)
##3
#class Student:
#    branch = 'cse'
#    count = 0                                                                   #Class member
#    def __init__(self,name,age,year):                                           #Constructer
#        self.name = name                                                        #Object member
#        self.age = age
#        self.year = year
#        Student.count = Student.count +  1
#
#    def get_name(self):
#        print(self.name)
#
#    def get_age(self):
#        print(self.age)

#    def change_year(self):
#        self.year = self.year + 1
#s1 = Student('Roy' , 20 , 1)
#s1.get_name()
#s1.get_age()
#print(s1.year)
#s1.change_year()
#print(s1.year)

#s2 = Student('Ram' , 22 , 4)
#s2.get_name()
#s1.get_name()
#s2.get_age()
#print(s2.year)
#s2.change_year()
#print(s2.year)
#print(s1.branch)
#print(s2.branch)
#s1.branch = 'Mech'
#print(s2.branch)
#s2.branch = 'Civil'
#print(s1.branch)
#print(s2.branch)
#print(Student.count)

##3

#class Employee:
#    total_employee = 0
#    def __init__(self,name,salary):
#        self.name = name
#        self.salary = salary
#        Employee.total_employee = Employee.total_employee + 1
#
#    def display_employee(self):
#        print(self.name)
#        print(self.salary)
#
#    def display_count(self):
#
#e1 = Employee('Ram' , 20000)
#e1.display_employee()
#e1.display_count()
#
#e2 = Employee('Shyam' , 30000)
#e2.display_employee()
#e2.display_count()

##4 Single Inheritance

#class Parent:
#    def __init__(self):
#        print('calling parent constructer')
#    def parent_method(self):
#        print('calling parent method ')
#class Child(Parent):                                                           #Single inheritance syntax
#    def __init__(self):
#        print('calling child constructer')
#    def child_method(self):
#        print('calling child method')
#c = Child()
#c.child_method()
#c.parent_method()
#p = Parent()
#p.parent_method()
#p.child_method()

##5 Stack Implementation
#class Stack:
#        self.item = []
#    def isempty(self):
#        return self.item == []
#    def push(self,n):
#        self.item.append(n)
#    def pop(self):
#        return self.item.pop()
#    def size(self):
#        return len(self.item)
#s = Stack()
#print(s.isempty())
#s.push(10)
#s.push(20)
#s.push(30)
#print("Size of Stack :- %d " %s.size())
#print(s.pop() , s.pop() , s.pop() )

#class Person:
#    def __init__(self,first,last):
#        self.firstname = first
#        self.lastname = last
#    def get_name(self):
#        return self.firstname + ' ' + self.lastname
#class Employee(Person):
#    def __init__(self,first,last,empid):
#        super().__init__(first,last)                           ##Or             Person.__init__(self,fist,last)
#        self.empid = empid
#    def get_emp(self):
#        return self.get_name() + " " + self.empid
#p = Person('virat','kholi')
#e = Employee('Leo' , 'Messi' , '1007')
#print(p.get_name())
#print(e.get_emp())
###############Sum of four numbers############################
#n = []
#for i in range(0,4):
#    a = int(input('Enter nos.: '))
#    n.append(a)
#s = 0
#for ele in n:
#    s = s + ele
#print(s)
#
#numArray = map(int, input().split()) # Get the input
#sum_integer = 0

#for number in numArray:
#    sum_integer += number
#print(sum_integer)
########### Extend examples############################
#a = [10,20,30]
#b = ['A','B','C']
#a.extend(b)
#print(a)
############ Pop example #############################
#a = [10,20,30]
#b = ['A','B','C']
#a.pop(1)
#print(a)
############ Remove example #########################
a=[10 , 20 , 'cow' , 'ram' , 4.5 , 'cOw']
a.remove('cOw')
print(a)
############
