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

#============ Insert Example ==================
a = [10, 20, 30 ]
a.insert(1,40)
print(a)
a.insert(3,'Ram')
print(a)
