from flask import Blueprint, render_template

views = Blueprint(__name__, "view")

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/about_us")
def about_us():
    return render_template("about_us.html")

@views.route("/quiz/workout")
def quiz():
    return render_template("quiz.html")

@views.route("/recipies")
def common_recipies():
    return render_template("Common Recipies.html")


@views.route("/quiz/learnWorkout")
def Workout_defi():
    return render_template("Workouts.html")

@views.route("/Vegetarian")
def Vegetarian():
    return render_template("Vegetarian.html")