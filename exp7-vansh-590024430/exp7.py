def find_max_min(seq):
 max_val = seq[0]
 min_val = seq[0]
 for num in seq[1:]:
 if num > max_val:
 max_val = num
 if num < min_val:
 min_val = num
 return max_val, min_val
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Max and Min:", find_max_min(nums))
def sum_of_cubes(n):
 total = 0
 for i in range(1, n):
 total += i**3
 return total
n = int(input("Enter a positive integer: "))
print("Sum of cubes:", sum_of_cubes(n))
def print_numbers(n):
 if n == 0:
 return
 print_numbers(n-1)
 print(n)
n = int(input("Enter n: "))
print_numbers(n)
def fib(n):
 if n <= 1:
 return n
 return fib(n-1) + fib(n-2)
def print_fib_series(n):
 for i in range(n):
 print(fib(i), end=" ")
n = int(input("Enter number of terms: "))
print_fib_series(n)
volume_cone = lambda r, h: (1/3) * 3.14159 * r**2 * h
r = float(input("Enter radius: "))
h = float(input("Enter height: "))
print("Volume of cone:", volume_cone(r, h))
max_min = lambda lst: (max(lst), min(lst))
lst = [10, 6, 8, 90, 12, 56]
print(max_min(lst))
def greet(name, message):
 print(f"{message}, {name}!")
greet(name="Alice", message="Hello")
def greet(name, message="Hi"):
 print(f"{message}, {name}!")
greet("Bob")
def add_numbers(*nums):
 total = sum(nums)
 print("Sum:", total)
add_numbers(2, 4, 6, 8)
