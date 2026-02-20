from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained ML model
model = pickle.load(open("model/budget_model.pkl", "rb"))


# ===============================
# HOME PAGE
# ===============================
@app.route("/")
def index():
    return render_template("index.html")


# ===============================
# DASHBOARD PAGE
# ===============================
@app.route("/dashboard")
def dashboard():

    # Load finance data
    df = pd.read_csv("data/event_data.csv")
    df = pd.read_csv("data/event_data.csv")
    
    

    # KPI calculations
    total_planned = df["Planned"].sum()
    total_actual = df["Actual"].sum()
    total_sponsorship = df["Sponsorship"].sum()

    variance = total_actual - total_planned

    # Risk analysis logic
    if variance > 0:
        risk_status = "HIGH RISK"
        risk_color = "#f87171"
        insight = "Spending has exceeded planned budget. Cost control required."
    else:
        risk_status = "SAFE"
        risk_color = "#4ade80"
        insight = "Spending is within planned limits. Budget is under control."

    return render_template(
        "dashboard.html",
        planned=total_planned,
        actual=total_actual,
        sponsorship=total_sponsorship,
        variance=variance,
        risk_status=risk_status,
        risk_color=risk_color,
        insight=insight
    )


# ===============================
# ML PREDICTION API
# ===============================
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


# ===============================
# RUN APP
# ===============================
if __name__ == "__main__":
    app.run(debug=True)