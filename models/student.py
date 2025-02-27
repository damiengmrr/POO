class student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = [] 

    def add_grade(self, grade):
        if 0 <= grade <= 20:
            self.grades.append(grade) # on ajoute la note a la liste
        else:
            raise ValueError("La note doit être entre 0 et 20.")
    def get_grades(self):  # methode pour obtenir les notes de l'etudiant
        return self.grades  # renvoie la liste des notes

    def __str__(self):  # methode pour afficher l'etudiant sous forme de chaine
        return f"{self.name}, {self.age} ans"  # renvoie le nom et l'age de l'etudiant