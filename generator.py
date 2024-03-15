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

    # Iterate over each exercise group
    for group in groups:
        print(f"\n{group}:")
        exercises = db.get_exercises_by_group(group)

        # Check if there are any exercises in the group
        if not exercises:
            print("No exercises found in this group.")
            continue

        # Display the list of exercises in the group
        for exercise in exercises:
            print(f"{exercise[0]}. {exercise[1]}")

        # Determine the range of exercise numbers for the group
        start_number = exercises[0][0]
        end_number = exercises[-1][0]

        # Prompt the user to choose two exercises from the group
        while True:
            selected_exercise_ids = input(
                f"Choose two exercises from the {group} group (enter numbers, separated by space): ").split()
            valid_selection = True

            # Validate if the exercise numbers are within the available range
            for exercise_id in selected_exercise_ids:
                try:
                    exercise_id = int(exercise_id)
                    if not start_number <= exercise_id <= end_number:
                        print(
                            f"Invalid exercise number: {exercise_id}. Please choose within the available range.")
                        valid_selection = False
                        break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    valid_selection = False
                    break

            # Check if exactly two exercises were selected
            if valid_selection and len(selected_exercise_ids) == 2:
                break

        # Prompt the user to input the number of series and repetitions for each exercise
        for exercise_id in selected_exercise_ids:
            try:
                exercise_id = int(exercise_id)
                selected_exercise = [exercise for exercise in exercises if exercise[0] == exercise_id][0]

                # Prompt the user for the number of series
                while True:
                    try:
                        series = int(input(f"How many series of exercise '{selected_exercise[1]}'? "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter numbers only.")

                # Prompt the user for the number of repetitions
                while True:
                    try:
                        repetitions = int(
                            input(f"How many repetitions in each series of exercise '{selected_exercise[1]}'? "))
                        break
                    except ValueError:
                        print("Invalid input. Please enter numbers only.")

                selected_exercises[selected_exercise[1]] = {'series': series, 'repetitions': repetitions}
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    return selected_exercises


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
