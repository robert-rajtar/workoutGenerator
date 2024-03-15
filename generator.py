import sqlite3
from fpdf import FPDF


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
    return input("Enter the name of the person for whom the training will be: ")


def select_exercises(db, groups):
    selected_exercises = {}

    for group in groups:
        exercises = db.get_exercises_by_group(group)
        if not exercises:
            print("No exercises found in this group.")
            continue

        print_exercises(exercises)
        selected_exercise_ids = get_user_selected_exercises(exercises)
        selected_exercises.update(get_exercise_details(exercises, selected_exercise_ids))

    return selected_exercises


def print_exercises(exercises):
    print(f"\n{exercises[0][1]}:")
    for exercise in exercises:
        print(f"{exercise[0]}. {exercise[1]}")


def get_user_selected_exercises(exercises):
    start_number = exercises[0][0]
    end_number = exercises[-1][0]
    while True:
        selected_exercise_ids = input(f"Choose two exercises from the group (enter numbers, " 
                                      "separated by space): ").split()
        if validate_exercise_ids(selected_exercise_ids, start_number, end_number):
            return selected_exercise_ids


def validate_exercise_ids(selected_exercise_ids, start_number, end_number):
    if len(selected_exercise_ids) != 2:
        print("Please select exactly two exercises.")
        return False
    for exercise_id in selected_exercise_ids:
        try:
            exercise_id = int(exercise_id)
            if not start_number <= exercise_id <= end_number:
                print(f"Invalid exercise number: {exercise_id}. Please choose within the available range.")
                return False
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            return False
    return True


def get_exercise_details(exercises, selected_exercise_ids):
    exercise_details = {}
    for exercise_id in selected_exercise_ids:
        exercise_id = int(exercise_id)
        selected_exercise = next(exercise for exercise in exercises if exercise[0] == exercise_id)
        series, repetitions = get_series_and_repetitions(selected_exercise[1])
        exercise_details[selected_exercise[1]] = {'series': series, 'repetitions': repetitions}
    return exercise_details


def get_series_and_repetitions(exercise_name):
    series = int(input(f"How many series of exercise '{exercise_name}'? "))
    repetitions = int(input(f"How many repetitions in each series of exercise '{exercise_name}'? "))
    return series, repetitions


def generate_pdf(name, selected_exercises, pdf_report):
    pdf_report.add_page()
    pdf_report.set_font("Arial", style="", size=12)
    pdf_report.write_text(f"Exercise set for: {name}\n\n")

    for exercise, details in selected_exercises.items():
        text = f"Exercise: {exercise}, Series: {details['series']}, Repetitions: {details['repetitions']}\n"
        pdf_report.write_text(text)

    pdf_report.save()


def main():
    db = ExerciseDatabase('exercises.db')
    pdf_report = PDFReport('training_plan.pdf')

    name = get_user_name()
    groups = ['Leg Exercises', 'Chest Exercises', 'Back Exercises', 'Arm Exercises']
    selected_exercises = select_exercises(db, groups)
    generate_pdf(name, selected_exercises, pdf_report)

    db.close()


if __name__ == "__main__":
    main()
