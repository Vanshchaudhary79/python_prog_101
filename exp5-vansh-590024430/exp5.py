s = input("Enter a string: ")
count = sum(1 for ch in s if ch.isupper())
print("Number of capital letters:", count)
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)
s = input("Enter a string: ").lower()
vowels = "aeiou"
count = sum(1 for ch in s if ch in vowels)
print("Number of vowels:", count)
string = input("Enter the main string: ")
substring = input("Enter the substring: ")
count = string.count(substring)
print("Number of occurrences:", count)
s = input("Enter a string: ").upper()
freq = {}
for ch in s:
 if ch.isalpha():
 freq[ch] = freq.get(ch, 0) + 1
for k, v in freq.items():
 print(f"{v}{k}")
sentence = input("Enter a sentence: ")
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))
n = int(input("Enter number of fruits in each set: "))
s1 = {input(f"Enter fruit {i+1} for set1: ") for i in range(n)}
s2 = {input(f"Enter fruit {i+1} for set2: ") for i in range(n)}
print("Fruits in both sets:", s1 & s2)
print("Fruits only in s1:", s1 - s2)
print("Total fruits in s1 and s2:", len(s1 | s2))
S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}
print("Union:", S1 | S2)
print("Intersection:", S1 & S2)
print("Difference (S1 - S2):", S1 - S2)
print("Difference (S2 - S1):", S2 - S1)
print("Symmetric Difference:", S1 ^ S2)
