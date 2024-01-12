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