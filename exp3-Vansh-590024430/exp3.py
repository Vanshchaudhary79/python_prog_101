num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
 print("Number is divisible by both 3 and 5")
else:
 print("Number is not divisible by both 3 and 5")
num = int(input("Enter a number: "))
if num % 5 == 0:
 print("Number is a multiple of 5")
else:
 print("Number is not a multiple of 5")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
 print("Greatest number is:", a)
elif b > a:
 print("Greatest number is:", b)
else:
 print("Numbers are equal")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
 print("Greatest number is:", a)
elif b > a and b > c:
 print("Greatest number is:", b)
else:
 print("Greatest number is:", c)
import math
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = b**2 - 4*a*c
if d > 0:
 root1 = (-b + math.sqrt(d)) / (2*a)
 root2 = (-b - math.sqrt(d)) / (2*a)
 print("Real and distinct roots:", root1, root2)
elif d == 0:
 root = -b / (2*a)
 print("Real and equal roots:", root)

  else:
 real = -b / (2*a)
 imag = math.sqrt(-d) / (2*a)
 print("Imaginary roots:", real, "+", imag, "i and", real, "-", imag, "i")
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
 print(year, "is a leap year")
else:
 print(year, "is not a leap year")
import datetime
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))
date = datetime.date(year, month, day)
next_date = date + datetime.timedelta(days=1)
print("Next date is:", next_date.day, next_date.month, next_date.year)
name = input("Enter student name: ")
roll = input("Enter roll number: ")
sapid = input("Enter SAP ID: ")
sem = input("Enter semester: ")
course = input("Enter course: ")
marks = {}
marks['PDS'] = int(input("Enter marks in PDS: "))
marks['Python'] = int(input("Enter marks in Python: "))
marks['Chemistry'] = int(input("Enter marks in Chemistry: "))
marks['English'] = int(input("Enter marks in English: "))
marks['Physics'] = int(input("Enter marks in Physics: "))
percentage = sum(marks.values()) / 5
cgpa = percentage / 10
if 0 <= cgpa <= 3.4:
 grade = "F"
elif 3.5 <= cgpa <= 5.0:
 grade = "C+"
elif 5.1 <= cgpa <= 6.0:
 grade = "B"
elif 6.1 <= cgpa <= 7.0:
 grade = "B+"
elif 7.1 <= cgpa <= 8.0:
 grade = "A"
elif 8.1 <= cgpa <= 9.0:
 grade = "A+"
elif 9.1 <= cgpa <= 10.0:
 grade = "O (Outstanding)"
else:
 grade = "Invalid CGPA"
print("\n--- Grade Sheet ---")
print("Name:", name)
print("Roll Number:", roll, "SAPID:", sapid)
print("Sem:", sem, "Course:", course)
print("\nSubject name: Marks")
for subject, mark in marks.items():
 print(subject + ":", mark)
print("Percentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)
