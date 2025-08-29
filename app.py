from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a secure key in production

# Dummy user data
users = {
    "john": {"password": "password123", "name": "John Doe"}
}

# Dummy workout data
workouts = [
    {"date": "2025-08-28", "exercise": "Bench Press", "reps": 10, "sets": 3},
    {"date": "2025-08-28", "exercise": "Squats", "reps": 12, "sets": 4},
]

# Dummy membership plans
plans = [
    {"name": "Basic Plan", "price": "$30/month"},
    {"name": "Premium Plan", "price": "$50/month"},
    {"name": "Pro Plan", "price": "$70/month"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)

        if user and user['password'] == password:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials. Try again.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please login to access the dashboard.', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html', workouts=workouts)

@app.route('/plans')
def view_plans():
    return render_template('plans.html', plans=plans)

if __name__ == '__main__':
    app.run(debug=True)
