Year = int(input("Enter: "))
if Year%4 != 0:
    print("Common")
elif Year%100 !=0:
    print("Leap year") 
elif Year%400!=0:
    Print("common")
else:
    print("Leap year")
