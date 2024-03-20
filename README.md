This project is a simple exercise planner that allows users to select exercises from different groups and generates a PDF training plan based on the user's selections.

Requirements
---------------------------
 - Python 3.x
 - sqlite3
 - fpdf
 - Flask

Installation
--------------------------------------------
Clone the repository: 
git clone https://github.com/robert-rajtar/workoutGenerator.git

Install the required packages: 
pip install fpdf Flask

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

Run the Flask application by executing the app.py file.

Access the exercise planner through a web browser.

Example
---------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, send_file

import sqlite3

from fpdf import FPDF


if __name__ == "__main__":

    app.run(debug=True)


