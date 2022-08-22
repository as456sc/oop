class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    

    def grades_for_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in self.courses_attached and course in self.evaluation_of_lecturers :
            if course in lecture.evaluation_of_lecturers:
                lecture.evaluation_of_lecturers[course] += [grade]
            else:
                lecture.evaluation_of_lecturers[course] = [grade]
        else:
            return 'Ошибка'
    
   
    s_grades= [5]
    average_grade = sum(s_grades)/len(s_grades)

    def __str__(self):
        return f"Имя: {self.name}\nФамиилия: {self.surname}\nСредняя оценка за домашнее задание{self.average_grade}\nКурсы в процессе изучения: Python, Git\nЗавершенные курсы:Введение в програмирование "  
    
    def __lt__(self, other):
        return self.s_grades < other.s_grades

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
      
    

class Lecture(Mentor):
    evaluation_of_lecturers = {}
     
    list_grades = [5] # 5 поставлено чтобы не было ошибки "ZeroDivisionError: division by zero"
    
    average = sum(list_grades)/len(list_grades) 
    
    def __str__(self):
       return f"Имя: {self.name}\nФамиилия: {self.surname}\nСредняя оценка: {self.average}" 
    
    def __lt__(self, other):
        return self.list_grades < other.list_grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def __str__(self ):
        return f"Имя: {self.name}\nФамиилия: {self.surname}"
               
    


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecture = Lecture('Some', 'Buddy')


cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
 
print(best_student.grades)

print(cool_mentor)
print(cool_lecture)
print(best_student)
print(list_grades < other.list_grades)

