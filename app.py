
import os
import subprocess
import sqlite3

from flask import Flask, request

app = Flask(__name__)

# Vulnerability 1: Hardcoded secret
API_SECRET_KEY = "DEMO_SECRET_DO_NOT_USE"

@app.route("/user")
def get_user():

    username = request.args.get("username")

    # Vulnerability 2: SQL injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)

    return "User query processed"


@app.route("/run")
def run_command():

    cmd = request.args.get("cmd")

    # Vulnerability 3: Command injection
    os.system(cmd)

    # Vulnerability 4: Insecure subprocess
    subprocess.call(cmd, shell=True)

    return "Command executed"


if __name__ == "__main__":
    app.run(debug=True)
