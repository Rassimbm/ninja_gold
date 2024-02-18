from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []
    return render_template("index.html", gold=session["gold"], activities=["activities"])


if __name__ == ("__main__"):
    app.run(debug=True)