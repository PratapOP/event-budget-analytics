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
    
    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # ===============================
    # CATEGORY ANALYSIS
    # ===============================
    category_summary = df.groupby("Category")["Actual"].sum()

    category_labels = category_summary.index.tolist()
    category_values = category_summary.values.tolist()

    # ===============================
    # MONTHLY TREND ANALYSIS
    # ===============================
    df["Month"] = df["Date"].dt.strftime("%b")

    monthly_summary = df.groupby("Month")["Actual"].sum()

    month_labels = monthly_summary.index.tolist()
    month_values = monthly_summary.values.tolist()

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
    
    # Top spending category
    top_category = category_summary.idxmax()

    executive_insight = (
        f"Highest spending category is {top_category}. "
        f"Consider optimizing costs here for better budget control."
    )


# ===============================
# ML PREDICTION API
# ===============================
@app.route("/predict", methods=["POST"])
def predict():
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

    # Convert date column
    df["Date"] = pd.to_datetime(df["Date"])

    # ===============================
    # CATEGORY ANALYSIS
    # ===============================
    category_summary = df.groupby("Category")["Actual"].sum()

    category_labels = category_summary.index.tolist()
    category_values = category_summary.values.tolist()

    # ===============================
    # MONTHLY TREND ANALYSIS
    # ===============================
    df["Month"] = df["Date"].dt.strftime("%b")

    monthly_summary = df.groupby("Month")["Actual"].sum()

    month_labels = monthly_summary.index.tolist()
    month_values = monthly_summary.values.tolist()

    # ===============================
    # KPI CALCULATIONS
    # ===============================
    total_planned = df["Planned"].sum()
    total_actual = df["Actual"].sum()
    total_sponsorship = df["Sponsorship"].sum()

    variance = total_actual - total_planned

    # ===============================
    # RISK ANALYSIS
    # ===============================
    if variance > 0:
        risk_status = "HIGH RISK"
        risk_color = "#f87171"
        insight = "Spending has exceeded planned budget. Cost control required."
    else:
        risk_status = "SAFE"
        risk_color = "#4ade80"
        insight = "Spending is within planned limits. Budget is under control."

    # ===============================
    # EXECUTIVE INSIGHT
    # ===============================
    top_category = category_summary.idxmax()

    executive_insight = (
        f"Highest spending category is {top_category}. "
        f"Consider optimizing costs here for better budget control."
    )

    # ===============================
    # RENDER DASHBOARD
    # ===============================
    return render_template(
        "dashboard.html",
        planned=total_planned,
        actual=total_actual,
        sponsorship=total_sponsorship,
        variance=variance,
        risk_status=risk_status,
        risk_color=risk_color,
        insight=insight,
        category_labels=category_labels,
        category_values=category_values,
        month_labels=month_labels,
        month_values=month_values,
        executive_insight=executive_insight
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