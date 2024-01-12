class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def grade_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in lecturer.courses_attached
            and course in self.courses_in_progress
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self):
        middle_grade = sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values()) / len(self.grades) if self.grades else 0
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {middle_grade:.1f}\n" \
               f"Курсы в процессе изучения: {in_progress_courses}\nЗавершенные курсы: {finished_courses}"
    
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()

    def calculate_average_grade(self):
        return (
            sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values())
            / len(self.grades) if self.grades else 0
        )

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        middle_grade = (sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values())
            / len(self.grades) if self.grades else 0)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {middle_grade:.1f}"
    
    def __lt__(self, other):
        return self.calculate_average_grade() < other.calculate_average_grade()

    def __le__(self, other):
        return self.calculate_average_grade() <= other.calculate_average_grade()

    def __eq__(self, other):
        return self.calculate_average_grade() == other.calculate_average_grade()

    def __ne__(self, other):
        return self.calculate_average_grade() != other.calculate_average_grade()

    def __gt__(self, other):
        return self.calculate_average_grade() > other.calculate_average_grade()

    def __ge__(self, other):
        return self.calculate_average_grade() >= other.calculate_average_grade()

    def calculate_average_grade(self):
        return (
            sum(sum(course_grades) / len(course_grades) for course_grades in self.grades.values())
            / len(self.grades) if self.grades else 0
        )

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
    
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


some_reviewer = Reviewer("Some", "Buddy")
print(some_reviewer)

some_lecturer = Lecturer("Some", "Buddy")
some_student = Student("Ruoy", "Eman", "male")
some_student.courses_in_progress.extend(["Python", "Git"])
some_lecturer.courses_attached.append("Python")
some_lecturer.rate_hw(some_student, "Python", 9.9)
some_lecturer.rate_hw(some_student, "Git", 9.9)
some_student.finished_courses.append("Введение в программирование")
some_student.grades["Python"] = [9.9]
some_student.grades["Git"] = [9.9]
print(some_lecturer)

print(some_student)

student1 = Student("John", "Dow", "male")
student2 = Student("Jane", "Dow", "female")

lecturer1 = Lecturer("Professor", "Snape")
lecturer2 = Lecturer("Professor", "Hagrid")

reviewer1 = Reviewer("Professor", "Dambldore")
reviewer2 = Reviewer("Professor", "Macgonagall")

reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Java", 9)
reviewer1.rate_hw(student2, "Python", 7)
reviewer1.rate_hw(student2, "Java", 7)

reviewer2.rate_hw(student1, "C+", 9)
reviewer2.rate_hw(student1, "Pascal", 8)
reviewer2.rate_hw(student2, "C+", 8)
reviewer2.rate_hw(student2, "Pascal", 7)

lecturer1.rate_hw(student1, "Python", 7)
lecturer1.rate_hw(student1, "Java", 8)
lecturer1.rate_hw(student2, "Python", 7)
lecturer1.rate_hw(student2, "Java", 6)

lecturer2.rate_hw(student1, "C+", 8)
lecturer2.rate_hw(student1, "Pascal", 7)
lecturer2.rate_hw(student2, "C+", 7)
lecturer2.rate_hw(student2, "Pascal", 7)

student1.grades["Python"] = [7, 8]
student1.grades["Java"] = [6, 8]

student2.grades["Python"] = [7, 9]
student2.grades["Java"] = [8, 8]

lecturer1.grades["Python"] = [8, 8]
lecturer1.grades["Java"] = [7, 8]

lecturer2.grades["C+"] = [8, 9]
lecturer2.grades["Pascal"] = [8, 8]

print("О студентах:")
print(student1)
print("\n--\n")
print(student2)

print("\nО лекторах:")
print(lecturer1)
print("\n--\n")
print(lecturer2)

print("\nСравнениваем оценки студентов:")
if student1 < student2:
    print(f"{student1.name} {student1.surname} имеет меньшую оценку.")
elif student1 > student2:
    print(f"{student1.name} {student1.surname} имеет большую оценку.")
else:
    print("Оценки студентов равны.")

print("\nСравнениваем лекторов:")
if lecturer1 < lecturer2:
    print(f"{lecturer1.name} {lecturer1.surname} имеет меньшую оценку за лекции.")
elif lecturer1 > lecturer2:
    print(f"{lecturer1.name} {lecturer1.surname} имеет большую оценку за лекции.")
else:
    print("Оценки лекторов равны.")

def average_grade(students, course_name):
    total_grades = 0
    total_students = 0

    for student in students:
        if course_name in student.grades:
            total_grades += sum(student.grades[course_name])
            total_students += sum(student.grades[course_name])
            
        if total_grades > 0:
            average_grade = total_grades / total_students
            return average_grade
        else:
            return None
        
def average_grade_lecturer(lecturers, course_name):
    total_grades = 0
    total_students = 0

    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grades += sum(lecturer.grades[course_name])
            total_lecturers += sum(lecturer.grades[course_name])

        if total_grades > 0:
            average_grade = total_grades / total_lecturers
            return average_grade
        else:
            return None