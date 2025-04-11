age= int(input())

if age<13:
    print("child")
elif age>13 and age <= 19:
         print("teen")
elif age>19 and age<=30:
              print("young")
elif age>30 and age<=60:
                   print("middle aged")
elif age>60:
                        print("old aged")
else:
    print("invalid input")