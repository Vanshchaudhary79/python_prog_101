num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
 fact *= i
print("Factorial:", fact)
num = int(input("Enter a number: "))
temp = num
sum_val = 0
while temp > 0:
 digit = temp % 10
 sum_val += digit ** 3
 temp //= 10
print("Armstrong Number" if sum_val == num else "Not Armstrong")
n = int(input("Enter number of terms: "))
a, b = 0, 1
print("Fibonacci Series:")
for _ in range(n):
 print(a, end=" ")
 a, b = b, a + b
print()
num = int(input("Enter a number: "))
if num > 1:
 for i in range(2, num):
 if num % i == 0:
 print("Not Prime")
 break
 else:
 print("Prime")
else:
 print("Not Prime")
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
 sum_digits += num % 10
 num //= 10
print("Sum of digits:", sum_digits)
count = 0
for i in range(1, 101):
 if i % 5 == 0 or i % 7 == 0:
 print(i, end=" ")
 count += 1
print("\nCount:", count)
s = input("Enter a string: ")
print("Uppercase:", s.upper())
print("Prime numbers between 1 and 100:")
for num in range(2, 101):
 for i in range(2, num):
 if num % i == 0:
 break
 else:
 print(num, end=" ")
print()
num = int(input("Enter a number: "))
for i in range(1, 11):
 print(f"{num} * {i} = {num * i}")
