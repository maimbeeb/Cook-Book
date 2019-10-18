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
    recipes = mongo.db.recipe.find()
    return render_template('index.html', recipes=recipes, cuisine=cuisine, category=category)


@app.route('/recipe/')
def recipe():
    cuisine = ["american", "chinese", "continental", "cuban", "french", "greek", "indian", "indonesian", "italian", "japanese",
               "korean", "lebanese", "malaysian", "mexican", "pakistani", "russian", "singapore", "spanish", "thai", "tibetan", "vietnamese"]

    category = ["appetizers, beverages", "soups, salads", "vegatables",
                "main dishes", "breads, rolls", "desserts", "miscellaneous"]

    # QUERY PARAM RECIPE ID
    key = request.args.get('recip')

    # RETRIEVE RECIPE FROM COLLECTION
    recipe = mongo.db.recipe.find({"_id": ObjectId(key)})
    return render_template('recipe.html', recipe=recipe, cuisine=cuisine, category=category)

@app.route('/search', methods=['GET', 'POST'])
def search():
    cuisine = ["american", "chinese", "continental", "cuban", "french", "greek", "indian", "indonesian", "italian", "japanese",
               "korean", "lebanese", "malaysian", "mexican", "pakistani", "russian", "singapore", "spanish", "thai", "tibetan", "vietnamese"]

    category = ["appetizers, beverages", "soups, salads", "vegatables",
                "main dishes", "breads, rolls", "desserts", "miscellaneous"]
    recipe_name = request.values.get("recipe")
    if recipe_name:
        recipes = mongo.db.recipe.find(
            {"recipe": {"$regex": recipe_name, "$options": "i"}})
        return render_template('index.html', recipes=recipes, recipe_name=recipe_name, cuisine=cuisine, category=category)
    else:
        return redirect("/")   

@app.route("/remove")
def remove():
    # DELETING A RECIPE WITH VARIOUS REFERENCES

    # RECIPE OBJECT KEY
    key = request.values.get("_id")

    # REMOVE DATA FROM COLLECTION
    mongo.db.recipe.remove({"_id": ObjectId(key)})
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
