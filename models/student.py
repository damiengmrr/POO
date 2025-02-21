class Student:
    def __init__(self, name, student_id, age):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        if (0 <= grade <= 20):
            self.grades.append(grade)
        else:
            print("Erreur : La note doit être comprise entre 0 et 20")


    def get_average_grade(self):
        #retourne la moyenne des notes de l'etudiant
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        #Retourne une representation sous forme de texte.
        return f"Étudiant: {self.name}, ID: {self.student_id}, Age: {self.age}, Moyenne: {self.get_average_grade():.2f}"