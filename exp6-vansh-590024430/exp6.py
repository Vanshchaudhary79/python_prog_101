n = int(input("Enter number of values: "))
values = [int(input(f"Enter value {i+1} (0-3): ")) for i in range(n)]
for i in range(4):
 print(f"{i} occurred {values.count(i)} times")
n = int(input("Enter number of values: "))
t = tuple(float(input(f"Enter value {i+1}: ")) for i in range(n))
avg = sum(t) / len(t)
print("Average:", avg)
n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))
unique_scores = sorted(set(scores), reverse=True)
runner_up = unique_scores[1]
print("Runner-up score:", runner_up)
n = int(input("Enter number of persons: "))
students = {input("Enter name: "): input("Enter city: ") for _ in
range(n)}
print("All names:", list(students.keys()))
print("All cities:", list(students.values()))
print("Name and city of all students:")
for name, city in students.items():
 print(name, ":", city)
city_count = {}
for city in students.values():
 city_count[city] = city_count.get(city, 0) + 1
print("Students per city:", city_count)
n = int(input("Enter number of movies: "))
movies = {}
for i in range(n):
 name = input("Enter movie name: ")
 year = int(input("Enter release year: "))
 director = input("Enter director name: ")
 cost = float(input("Enter production cost: "))
 earning = float(input("Enter collection made: "))
 movies[name] = {"year": year, "director": director, "cost": cost,
"earning": earning}
print("\nAll movie details:")
for name, details in movies.items():
 print(name, ":", details)
print("\nMovies released before 2015:")
for name, details in movies.items():
 if details["year"] < 2015:
 print(name)
print("\nMovies that made a profit:")
for name, details in movies.items():
 if details["earning"] > details["cost"]:
 print(name)
director_name = input("\nEnter director name to search: ")
print("Movies directed by", director_name, ":")
for name, details in movies.items():
 if details["director"].lower() == director_name.lower():
 print(name)
