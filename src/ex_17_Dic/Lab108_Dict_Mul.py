student_infor1 = {
    "name": "Rose",
    "age": 100,
    "address": {
        "home_address": "ND",
        "office_address": "CA"
    }

}

print(student_infor1)

student_infor2 = {
    "name": "Amit",
    "age": 69,
    "address": {
        "home_address": "Goa",
        "office_address": "KA"
    }
}

print(student_infor2)

# list of two list

student_list = [student_infor1, student_infor2]
print(student_list)
print(student_list[0])
print(student_list[0]["name"])
print(student_list[0]["address"]["office_address"])