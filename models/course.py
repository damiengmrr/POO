class Course:
    def __init__(self, course_name, course_code, credit_hours):
        self.course_name = course_name
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.students = []  #liste pour stocker les etudiant inscrit

    def enroll_student(self, student):
        #ajoute un etudiant au cours
        self.students.append(student)

    def get_enrolled_students(self):
        #retourne la liste des etudiant inscrit
        return [str(student) for student in self.students]

    def __str__(self):
        #retourne une representation sous forme de texte
        return f"Cours: {self.course_name}, Code: {self.course_code}, Crédits: {self.credit_hours}"