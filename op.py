from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json

app = Flask(__name__)
app.secret_key = 'supersecretkey'

DB_FILE = 'db.json'

def load_db():
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({"users": {}, "appointments": []}, f)
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = load_db()

        if username in db['users']:
            flash('Username already exists.')
            return render_template('signup.html')
        db['users'][username] = password
        save_db(db)
        flash('Signup successful. Please login.')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = load_db()
        if db['users'].get(username) == password:
            session['user'] = username
            return redirect(url_for('patient_portal'))
        flash('Invalid credentials.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out.')
    return redirect(url_for('login'))

@app.route('/patient', methods=['GET', 'POST'])
def patient_portal():
    if 'user' not in session:
        return redirect(url_for('login'))

    db = load_db()
    username = session['user']

    status = None
    for appt in db['appointments']:
        if appt['username'] == username:
            status = appt['status']
            break

    return render_template('patient_home.html', username=username, status=status)

@app.route('/book', methods=['POST'])
def book():
    if 'user' not in session:
        return redirect(url_for('login'))

    data = request.form
    db = load_db()

    db['appointments'].append({
        "username": session['user'],
        "doctor": data['doctor'],
        "date": data['date'],
        "time": data['time'],
        "symptoms": data['symptom'],
        "status": "pending"
    })

    save_db(db)
    flash("Appointment booked successfully.")
    return redirect(url_for('patient_portal'))

@app.route('/doctor', methods=['GET', 'POST'])
def doctor():
    db = load_db()
    if request.method == 'POST':
        username = request.form['username']
        decision = request.form['decision']
        for appt in db['appointments']:
            if appt['username'] == username:
                appt['status'] = decision
                break
        save_db(db)
        flash(f"Updated {username}'s status to {decision}.")
        return redirect(url_for('doctor'))

    return render_template('doctor.html', appointments=db['appointments'])

# ✅ THIS WAS MISSING
if __name__ == '__main__':
    app.run(debug=True)
