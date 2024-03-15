import sqlite3

# Tworzenie bazy danych
conn = sqlite3.connect('exercises.db')
c = conn.cursor()

# Tworzenie tabeli ćwiczeń
c.execute('''CREATE TABLE IF NOT EXISTS exercises
             (id INTEGER PRIMARY KEY,
             group_name TEXT NOT NULL,
             name TEXT NOT NULL,
             description TEXT)''')

# Lista ćwiczeń na klatkę piersiową
chest_exercises = [
    ("Push-ups", "Strength exercise for chest and arms."),
    ("Bench Press", "Strength exercise for chest, shoulders, and triceps."),
    ("Dumbbell Flyes", "Isolation exercise for chest muscles."),
    ("Cable Crossovers", "Isolation exercise for chest muscles."),
    ("Incline Dumbbell Press", "Strength exercise for upper chest muscles."),
    ("Dips", "Strength exercise for chest and triceps."),
    ("Flat Bench Dumbbell Press", "Strength exercise for chest and shoulders."),
    ("Incline Bench Press", "Strength exercise for chest muscles."),
    ("Elevated Push-ups", "Strength exercise for chest and upper chest muscles."),
    ("Incline Dumbbell Flyes", "Strength exercise for chest and shoulders.")
]

# Lista ćwiczeń na plecy
back_exercises = [
    ("Pull-ups", "Strength exercise for back muscles."),
    ("Deadlift", "Strength exercise for back, glutes, and legs."),
    ("Barbell Rows", "Strength exercise for back and arms."),
    ("Sumo Deadlift", "Deadlift variation mainly targeting leg muscles."),
    ("Barbell Bent-over Rows", "Strength exercise for back and arms."),
    ("Dumbbell Rows", "Strength exercise for back and arms."),
    ("One-arm Dumbbell Rows", "Strength exercise for back and arms."),
    ("Cable Pulldowns", "Isolation exercise for back muscles."),
    ("Lat Pulldowns", "Isolation exercise for back muscles."),
    ("Dumbbell Rows on an Incline Bench", "Strength exercise for back and arms.")
]

# Lista ćwiczeń na ramiona
arms_exercises = [
    ("Standing Dumbbell Press", "Strength exercise for arms and shoulders."),
    ("Dumbbell Bicep Curls", "Strength exercise for biceps."),
    ("French Press", "Isolation exercise for triceps."),
    ("Lateral Raises", "Strength exercise for shoulder muscles."),
    ("Triceps Kickbacks", "Strength exercise for triceps."),
    ("Dumbbell Shoulder Press", "Strength exercise for arms and shoulders."),
    ("Hammer Curls", "Strength exercise for biceps."),
    ("Seated Dumbbell Press", "Strength exercise for arms and shoulders."),
    ("Preacher Curls", "Strength exercise for biceps."),
    ("Standing One-arm Barbell Press", "Strength exercise for arms and shoulders.")
]

# Lista ćwiczeń na nogi
legs_exercises = [
    ("Barbell Squats", "Strength exercise for leg muscles."),
    ("Walking Lunges", "Strength exercise for leg muscles."),
    ("Standing Calf Raises", "Strength exercise for calf muscles."),
    ("Straight-leg Deadlift", "Strength exercise for leg muscles, glutes, and back."),
    ("Leg Extensions", "Isolation exercise for quadriceps."),
    ("Leg Curls", "Isolation exercise for hamstrings."),
    ("Leg Press", "Isolation exercise for quadriceps."),
    ("Sumo Squats", "Squat variation mainly targeting inner thigh muscles."),
    ("Machine Calf Raises", "Strength exercise for calf muscles."),
    ("Half Squats", "Strength exercise for leg muscles.")
]

# Dodawanie ćwiczeń do bazy danych
for exercise in chest_exercises:
    c.execute("INSERT INTO exercises (group_name, name, description) VALUES (?, ?, ?)", ('Chest Exercises',) + exercise)

for exercise in back_exercises:
    c.execute("INSERT INTO exercises (group_name, name, description) VALUES (?, ?, ?)", ('Back Exercises',) + exercise)

for exercise in arms_exercises:
    c.execute("INSERT INTO exercises (group_name, name, description) VALUES (?, ?, ?)", ('Arm Exercises',) + exercise)

for exercise in legs_exercises:
    c.execute("INSERT INTO exercises (group_name, name, description) VALUES (?, ?, ?)", ('Leg Exercises',) + exercise)

# Zatwierdzenie zmian i zakończenie połączenia z bazą danych
conn.commit()
conn.close()
