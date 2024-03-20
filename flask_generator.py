from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from fpdf import FPDF

app = Flask(__name__)

class ExerciseDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def get_exercises_by_group(self, group):
        self.cur.execute("SELECT id, name FROM exercises WHERE group_name=?", (group,))
        exercises = self.cur.fetchall()
        return exercises

    def close(self):
        self.conn.close()

class PDFReport:
    def __init__(self, file_name):
        self.pdf = FPDF()
        self.file_name = file_name

    def add_page(self):
        self.pdf.add_page()

    def set_font(self, font_family, style, size):
        self.pdf.set_font(font_family, style, size)

    def write_text(self, text):
        self.pdf.cell(200, 10, txt=text, ln=True)

    def save(self):
        self.pdf.output(self.file_name)

def get_user_name():
    return request.form['name']

def select_exercises(db, groups):
    selected_exercises = {}

    for group in groups:
        exercises = db.get_exercises_by_group(group)
        if not exercises:
            print("No exercises found in this group.")
            continue

        selected_exercise_ids = request.form.getlist(group)
        selected_exercises.update(get_exercise_details(exercises, selected_exercise_ids))

    return selected_exercises

def get_exercise_details(exercises, selected_exercise_ids):
    exercise_details = {}
    for exercise_id in selected_exercise_ids:
        exercise_id = int(exercise_id)
        selected_exercise = next(exercise for exercise in exercises if exercise[0] == exercise_id)
        series, repetitions = get_series_and_repetitions(selected_exercise[1])
        exercise_details[selected_exercise[1]] = {'series': series, 'repetitions': repetitions}
    return exercise_details

def get_series_and_repetitions(exercise_name):
    series = int(request.form[f"{exercise_name}_series"])
    repetitions = int(request.form[f"{exercise_name}_repetitions"])
    return series, repetitions

def generate_pdf(name, selected_exercises, pdf_report):
    pdf_report.add_page()
    pdf_report.set_font("Arial", style="", size=12)
    pdf_report.write_text(f"Exercise set for: {name}\n\n")

    for exercise, details in selected_exercises.items():
        text = f"Exercise: {exercise}, Series: {details['series']}, Repetitions: {details['repetitions']}\n"
        pdf_report.write_text(text)

    pdf_report.save()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db = ExerciseDatabase('exercises.db')
        pdf_report = PDFReport('training_plan.pdf')

        name = get_user_name()
        groups = ['Leg Exercises', 'Chest Exercises', 'Back Exercises', 'Arm Exercises']
        selected_exercises = select_exercises(db, groups)
        generate_pdf(name, selected_exercises, pdf_report)

        db.close()
        return redirect(url_for('index'))  # Redirect to the index page after processing the form

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
