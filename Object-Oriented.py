import re

#Part 1: Class Definition

#class of student
class student:
    def __init__(self, name='', email=''):
        self.name = name
        self.email = email
        self.grades = [] #ensures each student gets own list

#adds grades to the blank list above
    def add_grade(self, grade):
        self.grades.append(grade)

#gives the average of grades
    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
#shows all information for each student
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")

#Part 2:Working With Objects

#Create 3 student objects with initial grades

Student1 = student ("Annie", "annie@gmail.com")
Student1.grades[98, 75, 80]

Student2 = student ("Karl", "karl@Yahoo.com")
Student2.grades[81, 79, 92]

Student3 = student ("Walker", "walker@outlook.com")
Student3.grades[98, 94, 100]

#Adding 2 new grades for each student

Student1.add_grade(90)
Student1.add_grade(85)

Student2.add_grade(70)
Student2.add_grade(80)

Student3.add_grade(87)
Student3.add_grade(92)

#Printing the average of each student

students = [Student1, Student2, Student3]

for s in students:
    s.display_info()
    print(f"Average Grade: {s.average_grade()}")
    print("-" * 30)


#Part 3: Working With Objects

#dictionary
student_dict = {
    Student1.email: Student1,
    Student2.email: Student2,
    Student3.email: Student3
}

#get student email function

def get_student_by_email(email):
    return student_dict.get(email)

#Create a set of all unique grades

all_grades = set()
for student in student_dict.values():
    all_grades.update(student.grades)

print("All unique grades:", all_grades)

#Part 4: Tuple Practice

#method for returning grades as a tuple

def grades_tuple(self):
    return tuple(self.grades)

# try/except

grades_as_tuple = student.grades_tuple()
print("Grades as tuple:", grades_as_tuple)

try:
    grades_as_tuple[0] = 999
except TypeError:
    print("Tuples are immutable, their values cannot be changed.")

#Part 5: List Operations

#Removing the last grade from each student using .pop()

for student in students:
    removed = student.grades.pop()
    print(f"Removed last grade({removed}) from {student.name}")

#Accessing the first and last grade for each student

for Student in students:
    if student.grades:
        first = student.grades[0]
        last = student.grades[-1]
        print(f"{student.name}'s first grade: {first}")
        print(f"{student.name}'s last grade: {last}")
    else:
        print(f"{student.name} has no grades left.")

#Print the number of grades for each student

for student in students:
    print(f"{student.name} has {len(student.grades)} grades.")

    