n1=int(input("Enter number1: "))
n2=int(input("Enter number2: "))
n3=int(input("Enter number3: "))
if n1>n2 and n1>n3:
    print(f"Largest number:{n1}")
elif n2>n1 and n2>n3:
    print(f"Largest number:{n2}")
else:
    print(f"Largest number:{n3}")
       
