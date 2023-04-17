def avg_grades(grades):
    all_grades =[]
    for key in grades:
        all_grades.extend(grades[key])
        average_grade = sum(all_grades) / len(all_grades)
        return average_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    

    def rate_rw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        

    def __str__(self):
        self.all_grades =[]
        for key in self.grades:
            self.all_grades.extend(self.grades[key])
        self.average_grade = sum(self.all_grades) / len(self.all_grades)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {round(self.average_grade,2)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {','.join(self.finished_courses)}")
    

    def __eq__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип Student")
        self.average_grade = avg_grades(self.grades)
        self.average_grade_other = avg_grades(other.grades)
        return self.average_grade == self.average_grade_other
    
    def __lt__(self, other):
        if not isinstance(other, (int, Student)):
            raise TypeError("Операнд справа должен иметь тип Student")
        self.average_grade = avg_grades(self.grades)
        self.average_grade_other = avg_grades(other.grades)
        return self.average_grade < self.average_grade_other
        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def rate_hw(self, student, course, grade):
        print('Лекторы не могут выставлять оценки')

    def __str__(self):
        self.all_grades =[]
        for key in self.grades:
            self.all_grades.extend(self.grades[key])
        self.average_grade = sum(self.all_grades) / len(self.all_grades)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(self.average_grade,2)}"
    
    def __eq__(self, other):
        if not isinstance(other, (int, Lecturer)):
            raise TypeError("Операнд справа должен иметь тип Lecturer")
        self.average_grade = avg_grades(self.grades)
        self.average_grade_other = avg_grades(other.grades)
        return self.average_grade == self.average_grade_other
    
    def __lt__(self, other):
        if not isinstance(other, (int, Lecturer)):
            raise TypeError("Операнд справа должен иметь тип Lecturer")
        self.average_grade = avg_grades(self.grades)
        self.average_grade_other = avg_grades(other.grades)
        return self.average_grade < self.average_grade_other


class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def avg_stud_grade(stud_list, course):
    grades = []
    for student in stud_list:
        if course in student.grades:
            grades.extend(student.grades[course])
    return f'Средняя оценка за курс {course}: {sum(grades) / len(grades)}'


def avg_Lect_grade(lect_list, course):
    grades = []
    for lecturer in lect_list:
        if course in lecturer.grades:
            grades.extend(lecturer.grades[course])
    return f'Средняя оценка за курс {course}: {sum(grades) / len(grades)}'



# Практика

best_student = Student('Ruoy', 'Eman', 'your_gender')
second_student = Student('Jon', 'Fishman', 'male')
best_student.courses_in_progress += ['Python', 'C++', 'C#']
second_student.courses_in_progress +=['Java', 'Python']

second_lecturer = Lecturer('King', 'Kong')
second_lecturer.courses_attached += ['Python', 'Java', 'C++', 'C#']
 
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python', 'Java', 'C++', 'C#']
cool_reviewer = Reviewer('Roman', 'Erashov')
cool_reviewer.courses_attached += ['Python', 'Java', 'C++', 'C#']
second_reviewer = Reviewer('Ivan', 'Nagorniy')
cool_reviewer.courses_attached += ['Python', 'Java', 'C++', 'C#', 'SQL']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'C++', 9)
cool_reviewer.rate_hw(best_student, 'C#', 7)
cool_reviewer.rate_hw(second_student, 'Python', 8)

best_student.rate_rw(cool_lecturer, 'Python', 8)
best_student.rate_rw(cool_lecturer, 'Python', 5)
second_student.rate_rw(second_lecturer, 'Python', 10)
second_student.rate_rw(second_lecturer, 'Python', 7)

print(cool_lecturer)
print(second_lecturer)
print(best_student)
print(second_student)
print(cool_reviewer)
print(second_reviewer)
print(cool_lecturer > second_lecturer)
print(best_student == second_student)
