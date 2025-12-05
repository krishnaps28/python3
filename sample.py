#print(10//3)
#print(2**2)



#a=10
#a/=1
#print(a)



#a=10
#print(a==10)
#a=10
#b=10
#print(a is  b)
#a="hello"
#print("e" in a)



#a=3
#if(a%2==0):
#    print(a,"is even")
#else:
#    print(a, " is odd")





#a=int(input("enter first number :"))
#b=int(input("enter second number :"))
#c=int(input("enter third number :"))
#if a>b:
 #   if a>c:
  # else:
   #     print(c,"is laarger")
#else:
 #   if b>c:
  #      print(b, "is larger")
   # else:
    #    print(c ,"is larger")





#price=float(input("enter the cost price :"))
#if price > 100000:
 #   tax= price*0.15
#elif price >500000 and price <= 100000:
 #   tax=price*0.10
#else:
 #   tax=price*0.05
#print("tax to be paid",tax)






#a=int(input("enter first number :"))
#b=int(input("enter secomd number :"))
#c=int(input("enter third number :"))
#if a>b and a>c:
 #   print(a," is larger")
#elif b>a and b>c:
 #   print(b,"is greater")
#else:
 #   print(c,"is greater")






#city=str(input("enter thr city :"))
#if city==delhi:
 #   print("red fort")
#elif city==agra:
#    print("taj nahal")
#elif city==jaipur:
 #   print("jai mahal")
#else:
 #   print("no monument")





#day=int(input("enter the number :"))
#if day==1:
#3    print("sunday")
#   print("monday")
#f day==3:
 ####day==5:
    #print("thu")
#if day==6:
  #  print("fri")
#if day==7:
 #   print("sat")
#else:
 #   print("invalid")






#for i in range(1,11):
 #   print(i)

#   for j in range(4):
 ##  print()




#for i in range(1,101):
 #   if i%5==0:
  #      print("five")
   #    print(i)#





#for i in range(1,11):
 #  print(i*2)





#n=int(input("enter range :"))
#total=0
#for i in range(1,n):
#    total +=i
#print("sum :",total)






#n=int(input("enter a number :"))
#for i in range(1,11):
 #   print(n,"*",i,"=",n*i)





#n=int(input("enter a numbeer :"))
#count=0
#while n>0:
# n //=10
#  count=count+1
#print("digits",count)




#s=int(input("enter start :"))
#e=int(input("enter ending :"))
#for i in range(s,e):
#    if i%2 !=0:
#        print(i)





#for i in range(1,51):
 #   if i==25:
  #      continue
   # print(i)




s=int(input("enter the start range :"))
e=int(input("enter the end range :"))
even=0
odd=0
for i in range(s,e):
    if i%2==0:
        even +=1
    else:
        odd +=1
print("odd numbers ",odd)
print("even numbers ",even)