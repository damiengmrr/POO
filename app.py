from flask import Flask, jsonify, request
from models.student import student
from models.course import course
from models.enrollment import enrollment
from flask import Flask, jsonify, request, render_template # truc pour HTML CSS

app = Flask(__name__)  # creation de l'app
students = [] # liste qui stocke les etudiant 
course = []  # liste qui stocke les cours
enrollment = [] # liste qui stocke les inscriptions
@app.route("/")
def home():
    return render_template('index.html')  # Renvoie le template index.html

if __name__ == '__main__':
    app.run(debug=True)  # Démarre l'application avec le mode debug activé
    
@app.route('/student', methods=['GET'])  # route pour obtenir tous les etudiants
def get_students():
    return jsonify(student)  # renvoie la liste des etudiants en format JSON

@app.route('/student/<int:student_id>', methods=['GET'])  # route pour obtenir un etudiant avec son id
def get_student(student_id):
    student = next((s for s in student if s['id'] == student_id), None)  # chercher l'etudiant avec l'id
    if student is None:
        return jsonify({'message': 'étudiant pas trouvé'}), 404  # renvoie message d'erreur
    return jsonify(student)  # renvoie l'etudiant en format JSON

students = []  # une liste vide pour stocker les étudiants

@app.route('/student', methods=['POST'])
def add_student():
    new_student = request.get_json()  # obtenir les données de l'étudiant depuis la requête
    students.append(new_student)  # ajouter l'étudiant à la liste
    return jsonify(new_student), 201  # renvoie l'étudiant ajouté en format JSON avec code 201

@app.route('/course', methods=['GET'])  # route pour obtenir la liste des cours
def get_courses():
    return jsonify(course)  # renvoie la liste des cours en format JSON

@app.route('/course/<int:course_id>', methods=['GET'])  # route pour obtenir un cours avec son id
def get_course(course_id):
    course = next((c for c in course if c['id'] == course_id), None)  # chercher le cours avec l'id
    if course is None:  # si le cours est pas trouve
        return jsonify({'message': 'Cours non trouvé'}), 404  # renvoie message d'erreur
    return jsonify(course)  # renvoie le cours en format JSON

@app.route('/courses', methods=['POST'])  # route pour ajouter un cours
def add_course():
    new_course = request.get_json()  # obtenir les donnees du cours depuis la requete
    course.append(new_course)  # ajouter le cours a la liste
    return jsonify(new_course), 201  # renvoie le cours ajoute en format JSON avec code 201

@app.route('/enrollment', methods=['POST'])  # route pour inscrire un etudiant a un cours
def enroll_student():
    enrollment = request.get_json()  # obtenir les donnees de l'inscription depuis la requete
    student = next((s for s in student if s['id'] == enrollment['student_id']), None)  # verifier si l'etudiant existe
    course = next((c for c in course if c['id'] == enrollment['course_id']), None)  # verifier si le cours existe
    
    if student is None or course is None:  # si l'etudiant ou le cours est pas valide
        return jsonify({'message': 'Invalid student or course ID'}), 400  # renvoie message d'erreur
    enrollment.append(enrollment)  # ajouter l'inscription
    return jsonify(enrollment), 201  # renvoie l'inscription ajoutee en format JSON avec code 201

if __name__ == '__main__':  # si le fichier est execute directement
    app.run(debug=True)  # demarre l'app avec le mode debug