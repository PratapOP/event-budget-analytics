from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained ML model
model = pickle.load(open("model/budget_model.pkl", "rb"))

# Home page
@app.route("/")
def index():
    return render_template("index.html")


# Dashboard page
@app.route("/dashboard")
def dashboard():

    df = pd.read_csv("data/event_data.csv")

    total_planned = df["Planned"].sum()
    total_actual = df["Actual"].sum()
    total_sponsorship = df["Sponsorship"].sum()
    variance = total_actual - total_planned

    return render_template(
        "dashboard.html",
        planned=total_planned,
        actual=total_actual,
        sponsorship=total_sponsorship,
        variance=variance
    )


# ML prediction API
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    planned = float(data["planned"])
    actual = float(data["actual"])
    sponsorship = float(data["sponsorship"])

    prediction = model.predict([[planned, actual, sponsorship]])

    return jsonify({
        "over_budget": int(prediction[0])
    })


if __name__ == "__main__":
    app.run(debug=True)