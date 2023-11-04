number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
total = 0

for values in num_str:
    total = total + int(values) ** num_digits

if total == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
