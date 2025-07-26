from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
DB_FILE = "db.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def home():
    return render_template("patient.html")

@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()
    appointments = load_db()

    new_appt = {
        "name": data.get("name"),
        "doctor": data.get("doctor"),
        "date": data.get("date"),
        "time": data.get("time"),
        "symptoms": data.get("symptom"),
        "status": "pending"
    }

    appointments.append(new_appt)
    save_db(appointments)

    return "✅ Appointment booked successfully!", 200

@app.route("/check_status", methods=["POST"])
def check_status():
    data = request.get_json()
    name = data.get("name")

    appointments = load_db()
    for appt in appointments:
        if appt["name"].lower() == name.lower():
            return jsonify({"status": appt["status"]})
    return jsonify({"status": "Not Found"})

if __name__ == "__main__":
    app.run(debug=True)
