class enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
    def register(self):  # methode pour inscrire l'etudiant au cours
        self.course.enroll_student(self.student)  # on appelle la methode du cours pour inscrire l'etudiant

    def __str__(self):  # methode pour afficher l'inscription sous forme de chaine
        return f"{self.student.name} inscrit à {self.course.course_name}"  # renvoie le nom de l'etudiant et le nom du cours