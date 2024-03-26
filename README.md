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

Install the required packages

Usage
---------------------------------------------
Run the Flask application by executing the:

python3 app.py 

Access the exercise planner through a web browser.

Example
---------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, send_file

import sqlite3

from fpdf import FPDF


if __name__ == "__main__":

    app.run(debug=True)


