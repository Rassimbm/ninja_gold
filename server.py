from flask import Flask, session, render_template, request, redirect
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html", gold=session["gold"], activities=session["activities"])

@app.route("/process-money", methods=["POST"])
def process_money():
    locations = {
        "farm": {"min":10, "max": 20},
        "cave": {"min":5, "max": 10},
        "house": {"min":2, "max": 5},
        "casino": {"min":-50, "max": 28}
    }
    location = request.form["location"]
    earning = random.randint(locations[location]["min"], locations[location]["max"])
    time_stamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    if earning < 0:
        session["activities"].append({"message": f"You entered the {location} and lost {abs(earning)} golds... Ouch... {time_stamp}", "class": "loss"})
    else:
        session["activities"].append({"message": f"You earned {earning} golds from the {location}! {time_stamp}", "class": "win"})

    session["gold"] += earning
    return redirect("/")

@app.route("/reset-game")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ == ("__main__"):
    app.run(debug=True)