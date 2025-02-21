class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def register(self):
        #inscrit un etudiant a un cours
        self.course.enroll_student(self.student)

    def __str__(self):
        #retourne une representation sous forme de texte
        return f"{self.student.name} inscrit à {self.course.course_name}"