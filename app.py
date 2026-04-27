"""
Customer Relation Management Application
Author: Gattineni Neha
Stack: Python, Flask, MongoDB, Flask-Login
"""

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_pymongo import PyMongo
from flask_login import LoginManager, login_required, current_user
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "crm-secret-key")
app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/crm_db")

mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from routes.auth import auth_bp
from routes.customers import customers_bp
from routes.dashboard import dashboard_bp
from routes.admin import admin_bp

app.register_blueprint(auth_bp)
app.register_blueprint(customers_bp, url_prefix="/customers")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route("/")
def index():
    return redirect(url_for("dashboard.home"))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
