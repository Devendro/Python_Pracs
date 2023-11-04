a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

answer1 = (-b + (((b**2)-(4*a*c))**(1/2)))/(2*a)
answer2 = (-b - (((b**2)-(4*a*c))**(1/2)))/(2*a)

print(answer1)
print(answer2)
