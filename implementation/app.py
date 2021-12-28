# Python Standard Library Modules
from os import path
import pickle
# 3rd-party installed modules
from flask import Flask, render_template, request
# Custom Project Modules (*.py files)


# Load pre-fitted preprocessors, models, transformers
APP_DIR = path.dirname(path.abspath(__file__))

# repeat for each pickle file
#with open(f"{APP_DIR}/model/<FILENAME>", "r") as file:
    #variable_name = pickle.load(file)

# Define Flask app
app = Flask(__name__)

# Landing Page
@app.route("/")
def index():
    return render_template("project_landing.html")

# Prediction Form Page
@app.route("/predict", methods=["GET"])
def prediction_form():
    return render_template("project_form.html")

# Prediction Results Page
@app.route("/result", methods=["POST"])
def prediction_results():
    raw_form_data = request.form

    # Prep form data for model

    # Generate, transform, and format predictions

    # Render prediction
    return render_template(
        "project_return.html",
        # Make dynamic values available for rendering with template
        # key=value,
    )
