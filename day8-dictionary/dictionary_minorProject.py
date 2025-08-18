print("================== School Management System =================")

'''
** Instructions to follow **
- Store student records where the student ID is the key and the details(name, age, grades, contact info, etc.) are the value.

- Features:
* Add, update, delete student details.
* Search students by ID or name.
* Calculate average grades.

'''
students = {
    "101": {"name": "Aarav Sharma", "class": 10, "rollno": 1,
            "grade": "A", "gender": "Male", "city": "Kathmandu"},
    "102": {"name": "Sita Rai", "class": 10, "rollno": 2,
                    "grade": "B+", "gender": "Female", "city": "Pokhara"},
    "103": {"name": "Ram Karki", "class": 9, "rollno": 3,
                    "grade": "A-", "gender": "Male", "city": "Biratnagar"},
    "104": {"name": "Gita Thapa", "class": 9, "rollno": 4,
                    "grade": "B", "gender": "Female", "city": "Lalitpur"},
    "105": {"name": "Prakash Yadav", "class": 10, "rollno": 5,
                    "grade": "A", "gender": "Male", "city": "Janakpur"},
    "106": {"name": "Anita Gurung", "class": 8, "rollno": 6,
                    "grade": "B+", "gender": "Female", "city": "Pokhara"},
    "107": {"name": "Krishna Chaudhary", "class": 9, "rollno": 7,
                    "grade": "A", "gender": "Male", "city": "Dhangadhi"},
    "108": {"name": "Sunita Shrestha", "class": 10, "rollno": 8,
                    "grade": "A-", "gender": "Female", "city": "Kathmandu"},
    "109": {"name": "Dipesh KC", "class": 8, "rollno": 9,
                    "grade": "B", "gender": "Male", "city": "Nepalgunj"},
    "110": {"name": "Maya Lama", "class": 9, "rollno": 10,
                    "grade": "A", "gender": "Female", "city": "Hetauda"},
}


def add_student_profile():
    student_id = (input("What's student's id? ->").strip())
    student_name = input("Write student's name: ").strip().title()
    student_class = int(input("Write the student's class: ").strip())
    student_rollno = int(input("Write the student's roll no: ").strip())
    student_grade = input("Write student's grade: ").strip().upper()
    student_gender = input("Write student's gender: ").strip().title()
    student_city = input("Write the student's city: ").strip().title()

    if student_id != "" and student_name != "" and student_class != "" and student_rollno != "" and student_grade != "" and student_gender != "" and student_city != "":
        students[student_id] = {"name": student_name, "class": student_class, "roll_no": student_rollno,
                                "grade": student_grade, "gender": student_gender, "city": student_city}
        return print(students)
    else:
        print("You missed something to fill.")

# add_student_profile()



def update_student_data():
    sts_id = input("First, give me your id:").strip()
    if sts_id in students:
        print("What do you want to update?\n1.name\n2.class\n3.rollno\n4.gender\n5.city\n6.nothing")

        response = input("Please write here: ").lower()
        if response == "nothing":
            print("Thank you for visiting!")
            exit()
        value = input(f"What is your actual {response} ?")
        if response == "name":
            students[sts_id]["name"] = value
        elif response == "class":
            students[sts_id]["class"] = value
        elif response == "rollno":
            students[sts_id]["rollno"] = value
        elif response == "gender":
            students[sts_id]["gender"] = value
        elif response == "city":
            students[sts_id]["city"] = value
        else:
            print("Thank you!")
            exit()
    else:
        print("Your ID is not found!")
        exit()
    your_profile = {"name": students[sts_id]
                    ["name"], "class": students[sts_id]["class"], "rollno": students[sts_id]["rollno"], "gender": students[sts_id]["gender"], "city": students[sts_id]["city"]}
    return print("Your updated profile is here:\n", your_profile)

    '''
    idea: you have to first ask the id of the student, then you have to ask what does the student want to update? according to the answer of the student, I have to assign the value to the particular key. 
    '''
# update_student_data()



def delete_students_detail():
    
    ''' 
    ask id, search in the dict, if found the proceed ahead or say thank you!
    Ask student the record to be deleted, delete the record, update the new dict and display the updated dict
    '''


def search_student():
    pass


def average_grade():
    pass


def average_age():
    pass


# def start_me():
#     while True:
#         pass


# if __name__ == "__main__":
#     start_me()
