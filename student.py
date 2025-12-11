student=[]
while(True):
    print("""1.add
             2.viwe
             3.delete
             4.update
             5.exit""")
    choice=int(input("enter your choice :"))
    if choice==1:
        number=int(input("enter the numner of students that you want to add :"))
        for i in range(1,number+1):
            print('students :',i)
            adno=int(input(" enter addmno :"))
            name=input("enter name :")
            age=int(input("enter age :"))
            student.append([adno,name,age])
        print("added successfully")
    elif choice==2:
        for i in student:
            print(i)
    elif choice==3:
        adno=int(input("enter the addno for delete :"))
        for i in student:
            if i[10]==adno:
                student.remove(i)
                print("deleted successfully")
            else:
                print("student not found")
    elif choice==5:
        break
