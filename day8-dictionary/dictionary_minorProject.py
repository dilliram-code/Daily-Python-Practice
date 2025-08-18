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
    "101": {"name": "Aarav Sharma", "class": 10, "roll_no": 1,
            "grade": "A", "gender": "Male", "city": "Kathmandu"},
    "102": {"name": "Sita Rai", "class": 10, "roll_no": 2,
                    "grade": "B+", "gender": "Female", "city": "Pokhara"},
    "103": {"name": "Ram Karki", "class": 9, "roll_no": 3,
                    "grade": "A-", "gender": "Male", "city": "Biratnagar"},
    "104": {"name": "Gita Thapa", "class": 9, "roll_no": 4,
                    "grade": "B", "gender": "Female", "city": "Lalitpur"},
    "105": {"name": "Prakash Yadav", "class": 10, "roll_no": 5,
                    "grade": "A", "gender": "Male", "city": "Janakpur"},
    "106": {"name": "Anita Gurung", "class": 8, "roll_no": 6,
                    "grade": "B+", "gender": "Female", "city": "Pokhara"},
    "107": {"name": "Krishna Chaudhary", "class": 9, "roll_no": 7,
                    "grade": "A", "gender": "Male", "city": "Dhangadhi"},
    "108": {"name": "Sunita Shrestha", "class": 10, "roll_no": 8,
                    "grade": "A-", "gender": "Female", "city": "Kathmandu"},
    "109": {"name": "Dipesh KC", "class": 8, "roll_no": 9,
                    "grade": "B", "gender": "Male", "city": "Nepalgunj"},
    "110": {"name": "Maya Lama", "class": 9, "roll_no": 10,
                    "grade": "A", "gender": "Female", "city": "Hetauda"},
}


def add_student_profile():
    student_id = int(input("What's student's id? ->").strip())
    student_name = input("Write student's name: ").strip().title()
    student_class = int(input("Write the student's class: ").strip())
    student_rollno = int(input("Write the student's roll no: ").strip())
    student_grade = input("Write student's grade: ").strip().upper()
    student_gender = input("Write student's gender: ").strip().title()
    student_city = input("Write the student's city: ").strip().title()

    if student_id != "" and student_name != "" and student_class != "" and student_rollno != "" and student_grade != "" and student_gender != "" and student_city != "":
        students[student_id] = {"name": student_name, "class": student_class, "roll_no": student_rollno,
                                "grade": student_grade, "gender": student_gender, "city": student_city}
        return students
    else:
        print("You missed something to fill.")


updated_record = add_student_profile()
print(updated_record)


def update_student_data():
    pass


def delete_students_detail():
    pass


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
