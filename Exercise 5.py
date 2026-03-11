text = "Lourenz Angel A. Orcales"

length = len(text)

print("The length of the string is:", length)

print()

text = "BSIT - 1V"

count = 0
for char in text:
    count += 1

print("Total number of characters:", count)

print()

text = "Marjorie pikon"

first_char = text[0]

new_string = first_char + text[1:].replace(first_char, '$')

print("Modified string:", new_string)

print()

str1 = "Lourenz"
str2 = "Orcales"

new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]

print("Result:", new_str1 + " " + new_str2)

print()

a = "I"
b = "LOVE"
c = "YOU"
d = "SO MUCH"

result = a + " " + b + " " + c + " " + d

print(result)

print()

first_str = "Lourenz Angel"
second_str = "Orcales"

result = first_str + " " + second_str

print("Concatenated string:", result)

print()

name = "Lourenz Angel A. Orcales"
age = "19"

paragraph = "My name is " + name + " and I am " + age + " years old. I am currently studying programming and learning Python."

print(paragraph)