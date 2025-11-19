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

student_infor3 = {
    "name": "Peter",
    "age": 120,
    "address": {
        "home_address": "Podi",
        "office_address": "vizag"
        }
}

student_list = [student_infor1, student_infor2, student_infor3]
print(student_list)
print(student_list[2]["address"]["home_address"])