from flask import Flask, render_template, request, redirect
from gevent.pywsgi import WSGIServer
from flask_pymongo import PyMongo  # PYMONGO
from bson import ObjectId  # FOR OBJECTID TO WORK
from werkzeug.utils import secure_filename
import os
from datetime import datetime  # DATETIME
import base64

app = Flask(__name__)

# MONGO DB CONFIG
app.config["MONGO_URI"] = "mongodb://18.188.85.90:27098/cookbook"
mongo = PyMongo(app)

# APP ROOT
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# DEFAULT ROUTE - (HOME PAGE ROUTE)
@app.route('/')
def home():
    cuisine = ["american", "chinese", "continental", "cuban", "french", "greek", "indian", "indonesian", "italian", "japanese",
               "korean", "lebanese", "malaysian", "mexican", "pakistani", "russian", "singapore", "spanish", "thai", "tibetan", "vietnamese"]

    category = ["appetizers, beverages", "soups, salads", "vegatables",
                "main dishes", "breads, rolls", "desserts", "miscellaneous"]
    recipes = mongo.db.recipe.find()
    return render_template('index.html', recipes=recipes, cuisine=cuisine, category=category)

# INDIVIDUAL RECIPE DETAILS PAGE ROUTE
@app.route('/recipe', methods=['GET', 'POST'])
def recipe():
    # CUISINE LIST
    cuisine = ["american", "chinese", "continental", "cuban", "french", "greek", "indian", "indonesian", "italian", "japanese",
               "korean", "lebanese", "malaysian", "mexican", "pakistani", "russian", "singapore", "spanish", "thai", "tibetan", "vietnamese"]

    category = ["appetizers, beverages", "soups, salads", "vegatables",
                "main dishes", "breads, rolls", "desserts", "miscellaneous"]

    # QUERY PARAM RECIPE ID
    key = request.args.get('recip')

    # RETRIEVE RECIPE FROM COLLECTION
    recipe = mongo.db.recipe.find({"_id": ObjectId(key)})
    return render_template('recipe.html', recipe=recipe, cuisine=cuisine, category=category)

# SEARCH RECIPE
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

# REMOVE RECIPE FROM LIST ROUTE
@app.route("/remove")
def remove():
    # DELETING A RECIPE WITH VARIOUS REFERENCES

    # RECIPE OBJECT KEY
    key = request.values.get("_id")

    # REMOVE DATA FROM COLLECTION
    mongo.db.recipe.remove({"_id": ObjectId(key)})
    return redirect("/")

# ADD NEW RECIPE ROUTE
@app.route('/addRecipe', methods=['POST'])
def addRecipe():
    if request.method == 'POST':
        if request.files['image']:
            upload = request.files['image']
            rv = base64.b64encode(upload.read())  # bytes
            rv = rv.decode('ascii')
            rename_img = rv
        else:
            rename_img = ""

    # FORM VALUES RELATED TO RECIPE
    recipe_name = request.values.get("recipe")
    chef = request.values.get("chef")
    description = request.values.get("description")
    ingredients = request.values.get("ingredients")
    preparation = request.values.get("preparation")
    tools = request.values.get("tools")
    category = request.values.get("category")
    cuisine = request.values.get("cuisine")
    duration = request.values.get("duration")

    # INSERT RECIPE DETAILS IN COLLECTION
    mongo.db.recipe.insert({"recipe": recipe_name, "chef": chef, "description": description, "ingredients": ingredients, "preparation": preparation,
                            "tools": tools, "category": category, "cuisine": cuisine, "duration": duration, "created_date": datetime.now(), "image": rename_img})
    return redirect("/")

# UPDATE RECIPE ROUTE
@app.route('/updateRecipe', methods=['POST'])
def updateRecipe():

    # FORM VALUES RELATED TO RECIPE
    rename_img = request.values.get("imageKey")
    recipe_name = request.values.get("recipe")
    chef = request.values.get("chef")
    description = request.values.get("description")
    ingredients = request.values.get("ingredients")
    preparation = request.values.get("preparation")
    tools = request.values.get("tools")
    category = request.values.get("category")
    cuisine = request.values.get("cuisine")
    duration = request.values.get("duration")

    # UPDATE RECIPE DETAILS IN COLLECTION
    mongo.db.recipe.update({"_id": ObjectId(request.values.get("id"))}, {"$set": {"recipe": recipe_name, "chef": chef, "description": description, "ingredients": ingredients,
                                                                                  "preparation": preparation, "tools": tools, "category": category, "cuisine": cuisine, "duration": duration, "created_date": datetime.now(), "image": rename_img}})
    return redirect("/")


# __main__
if __name__ == '__main__':
    # app.run(debug=True)
    # app.run(host='0.0.0.0', port=80)
    # http_server = WSGIServer(('', 5000), app)
    # http_server.serve_forever()
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 7878)),
            debug=True)
