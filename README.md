

Student Management System

Ce projet implémente un système de gestion des étudiants en utilisant Flask et Python. L’API permet de gérer les informations des étudiants, y compris l’ajout d’un étudiant et la récupération des données.

Prérequis
	•	Python 3.x
	•	Flask
	•	Virtualenv (facultatif, mais recommandé pour gérer les dépendances)

Installation
	1.	Clone le repository ou télécharge le projet.

git clone <url-du-repository>

	2.	Crée un environnement virtuel et active-le.

python3 -m venv .venv
source .venv/bin/activate  # sur macOS ou Linux
.venv\Scripts\activate  # sur Windows

	3.	Installe les dépendances requises.

pip install -r requirements.txt

Lancer l’application

Une fois les dépendances installées, lance le serveur Flask avec la commande suivante :

flask run

L’API sera accessible sur http://127.0.0.1:5000.

Endpoints disponibles

1. Ajouter un étudiant
	•	Méthode : POST
	•	URL : /student
	•	Corps de la requête (format JSON) :

{
  "id": 1,
  "name": "Jean Dupont",
  "age": 20,
  "grades": [15, 18, 12]
}

	•	Réponse :

{
  "id": 1,
  "name": "Jean Dupont",
  "age": 20,
  "grades": [15, 18, 12]
}

2. Récupérer les informations d’un étudiant (par ID)
	•	Méthode : GET
	•	URL : /student/<id>
	•	Exemple : /student/1
	•	Réponse :

{
  "id": 1,
  "name": "Jean Dupont",
  "age": 20,
  "grades": [15, 18, 12]
}

Tests

Tu peux tester l’API avec des outils comme curl ou Postman. Par exemple, pour ajouter un étudiant avec curl :

curl -X POST http://127.0.0.1:5000/student \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "Jean Dupont", "age": 20, "grades": [15, 18, 12]}'

Structure du projet
	•	app.py : le fichier principal de l’application Flask.
	•	students.py : contient la logique de gestion des étudiants (par exemple, ajout et récupération des étudiants).
	•	requirements.txt : liste des dépendances nécessaires pour le projet.
