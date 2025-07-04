from flask import Flask, request, redirect, session, render_template_string
import re
import os


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default-unsafe-key")

# Load common passwords
with open("10-million-password-list-top-1000.txt", "r") as f:
    common_passwords = set(line.strip() for line in f)

# OWASP Level 1 password validation
def is_password_valid(password):
    if len(password) < 8:
        return False
    if password.lower() in common_passwords:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password", "")
        if is_password_valid(password):
            session["password"] = password
            return redirect("/welcome")
        return "Password does not meet requirements. <a href='/'>Try again</a>"
    
    return '''
    <form method="POST">
        <label>Password: <input type="password" name="password"></label>
        <button type="submit">Login</button>
    </form>
    '''

@app.route("/welcome")
def welcome():
    password = session.get("password")
    if not password:
        return redirect("/")
    return f'''
    <h1>Welcome!</h1>
    <p>Password: {password}</p>
    <a href="/logout">Logout</a>
    '''


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

