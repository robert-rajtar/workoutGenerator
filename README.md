This project is a simple exercise planner that allows users to select exercises from different groups and generates a PDF training plan based on the user's selections.

Requirements
---------------------------
 - Python 3.x
 - sqlite3
 - fpdf

Installation
--------------------------------------------
Clone the repository: 
git clone https://github.com/robert-rajtar/workoutGenerator.git

Install the required packages: 
pip install fpdf

Usage
---------------------------------------------
Ensure you have a SQLite database file containing exercises. The database should include a table named exercises with columns id, name, and group_name.
Import the ExerciseDatabase and PDFReport classes into your project.
Create an instance of ExerciseDatabase by providing the path to the database file.
Create an instance of PDFReport by specifying the desired PDF file name.
Utilize the provided functions to interact with the exercise planner:
 - get_user_name(): Prompts the user to enter the name of the person for whom the training will be designed.
 - select_exercises(db, groups): Enables the user to select exercises from predefined groups.
 - generate_pdf(name, selected_exercises, pdf_report): Generates a PDF training plan based on the user's selections.
Execute the main() function to run the exercise planner.

Example
---------------------------------------------
from exercise_planner import ExerciseDatabase, PDFReport, get_user_name, select_exercises, generate_pdf

db = ExerciseDatabase('exercises.db')
pdf_report = PDFReport('training_plan.pdf')

name = get_user_name()
groups = ['Leg Exercises', 'Chest Exercises', 'Back Exercises', 'Arm Exercises']
selected_exercises = select_exercises(db, groups)
generate_pdf(name, selected_exercises, pdf_report)

db.close()

