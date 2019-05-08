""""
dictionaries allows us to work with key value pairs.

"""

student = {"name":"john","age":25,"courses":["Math","CompSci"]}   # [math , compsci] is a list of in this case courses

print(student["courses"])

print(student.get("zipCode","Not Found"))  # you can especify error message

student["phone"] = "555-5555"              # adding a new entry to dictionary

print(student.get("phone","Not Found"))

# student.update({"name":"Jane","age":26,'phone':"555-5555"})         # updates a values
# #
# # print(student)

# del student["age"]# deletes values
# print(student)

#pop methos removes and return the value
# age = student.pop("age")
# print(student)
# print(age)

# print quantity of values in dict
print(len(student))
# see all of these keys
print(student.keys())
# see all of the values
print(student.values())
# see both values and keys
print(student.items())

for key,value in student.items():  # loop through
    print(key,value)