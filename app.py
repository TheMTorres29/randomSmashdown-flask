from flask import Flask, render_template, session, redirect, url_for, request
import random
from fighters import fighters
import secrets
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev_default_key")

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize session variables if not present
    if "remaining" not in session:
        session["remaining"] = fighters.copy()
        session["history"] = []
        session["last_selected"] = None

    message = ""
    # The currently displayed fighter is the last selected one
    selected = session.get("last_selected")

    if request.method == "POST":
        if session["remaining"]:
            # Select a new fighter at random
            new_selected = random.choice(session["remaining"])
            session["remaining"].remove(new_selected)
            # If there was a previously selected fighter, add it to history
            if session.get("last_selected"):
                session["history"].append(session["last_selected"])
            # Update last_selected to the new fighter
            session["last_selected"] = new_selected
            selected = new_selected
        else:
            message = "No more fighters!"
            # If there is a last selected fighter not in history, add it
            if session.get("last_selected") and session["last_selected"] not in session["history"]:
                session["history"].append(session["last_selected"])
            session["last_selected"] = None

    return render_template(
        "index.html",
        selected=selected,
        remaining=session["remaining"],
        history=session["history"],
        message=message
    )

@app.route("/reset")
def reset():
    # Clear all session variables to restart the app
    session.pop("remaining", None)
    session.pop("history", None)
    session.pop("last_selected", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)