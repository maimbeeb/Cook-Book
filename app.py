from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo  # PYMONGO
from bson import ObjectId  # FOR OBJECTID TO WORK
from werkzeug.utils import secure_filename
import os
from datetime import datetime  # DATETIME

app = Flask(__name__)

# MONGO DB CONFIG
app.config["MONGO_URI"] = "mongodb://localhost:27017/cookbook"
mongo = PyMongo(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def home():
    cuisine = ["american", "chinese", "continental", "cuban", "french", "greek", "indian", "indonesian", "italian", "japanese",
               "korean", "lebanese", "malaysian", "mexican", "pakistani", "russian", "singapore", "spanish", "thai", "tibetan", "vietnamese"]

    category = ["appetizers, beverages", "soups, salads", "vegatables",
                "main dishes", "breads, rolls", "desserts", "miscellaneous"]
    return render_template('index.html')
@app.route('/recipe/')
def recipe():
    return render_template('recipe.html')    
if __name__ == '__main__':
    app.run(debug=True)