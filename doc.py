# doc.py
from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
DB_FILE = "db.json"

# Load existing appointment data
def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

# Save updated appointment data
def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")  # Optional root route
def home():
    return "Welcome to the portal. Go to /doctor"

@app.route("/doctor")  # Show the dashboard
def doctor_portal():
    return render_template("doctor.html")

@app.route("/get_appointments")  # Return JSON list of appointments
def get_appointments():
    return jsonify(load_db())

@app.route("/update_status", methods=["POST"])  # Update status
def update_status():
    updated = request.get_json()
    data = load_db()
    for appt in data:
        if appt["name"] == updated["name"]:
            appt["status"] = updated["status"]
            break
    save_db(data)
    return "✅ Status updated!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
