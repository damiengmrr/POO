from models.student import Student
from models.course import Course
from models.enrollment import Enrollment

student1 = Student("Alice", "S123", 21)
student2 = Student("Bob", "S456", 22)

math_course = Course("Mathématiques", "101", 3)

# Inscription des étudiants au cours
enrollment1 = Enrollment(student1, math_course)
enrollment1.register()

enrollment2 = Enrollment(student2, math_course)
enrollment2.register()

student1.add_grade(12)
student1.add_grade(15)

student2.add_grade(15)
student2.add_grade(18)

# Afficher les résultats
print(student1)
print(student2)
print(math_course.get_enrolled_students())