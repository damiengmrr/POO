class course:
    def __init__(self, course_name, course_code, credit_hours):
        self.course_name = course_name
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.students = [] 
    def enroll_student(self, student):  #inscrire un étudiant
        self.students.append(student)  #ajoute l'etudiant a la liste des etudiant inscrit

    def get_enrolled_students(self):  #methode pour obtenir la liste des étudiants inscrits
        return [str(student) for student in self.students]  #renvoie une liste avec les noms des étudiants inscrits

    def __str__(self):  #afficher les informations du cours sous forme de chaine
        return f"Cours: {self.course_name}, Code: {self.course_code}, Crédits: {self.credit_hours}"  #renvoie les infos du cours