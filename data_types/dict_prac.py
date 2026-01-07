"""
This file holds the practice on Dictionary
"""

student_details = {
    "Alice": 100,
    "Bob": 20,
    "Donald": 2,
    "Mercy": 50,
    "Cedric": 60,
    "Ruth": 35
}

# iterating over keys
print("Iterating over keys")
for student in student_details:
    print(student)

for student in student_details.keys():
    print(student)

# iterating over values
print("Iterating over values")
for score in student_details.values():
    print(score)

# iterating over each key-value pair
print("Iterating over key-value pairs")
for key, value in student_details.items():
    print(f"student {key}: score {value}")

# sorting dictionary based on keys
attendance_order = sorted(student_details.items(), key=lambda item: item[0])
print(attendance_order)

# sorting dictionary based on values
rank_list = sorted(student_details.items(), key=lambda item: item[1], reverse=True)
print(rank_list)


# dictionary size cannot be modified with iteration, causes RuntimeError
for student in student_details:
    student_details["Johan"] = 45
