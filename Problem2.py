dog ={}
# printing an empty dictionary dog
print(dog)
dog = {
    "name": "Bunny", "colour": "Black", "Bread": "Bulldog", "Age": 2
}
print("dog dictionary:", dog)
# creating dictionary and adding keys to it
student = {
    "first_name": "durga sai teja", "last_name": "thota", "gender": "male",
    "age": 22, "marital_status": "Single", "skills": ["python"],
    "country": "India", "city": "Vissannapeta", "address": "9-410,Naidu vari veedhi,vissannapeta"
}
print("student dictionary:", student)
# printing length of the dictionary
print("Length of dictionary:", len(student))
# getting the value of skills and printing value of skills and data type of it
print("student skills:", student.get('skills'))
print(type(student['skills']))
# modifying skills  by adding another skill
student['skills'].insert(0, "java")
print("modifiying skills:", student)
# getting dictionary keys as list and printing keys as list
keys_List = list(student.keys())
print("keys_List:", keys_List)
# getting dictionary values as list and printing values as list
values_List = list(student.values())
print("values_List:", values_List)
