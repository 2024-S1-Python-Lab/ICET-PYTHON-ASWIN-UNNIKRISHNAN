import calc
num1=float(input("Enter a first number="))
num2=float(input("Enter a second number="))
sum=calc.add(num1,num2)
print(f"Addition:{sum}")
print(f"Substraction:{calc.substract(num1,num2)}")
print(f"Multiplication:{calc.multiply(num1,num2)}")
print(f"Division:{calc.divide(num1,num2)}")
