
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Message

main = Blueprint('main', __name__)

# Static demo login pages for employee and manager
@main.route("/employee_login")
def employee_login():
    return render_template("login.html")

@main.route("/manager_login")
def manager_login():
    return render_template("manager_login.html")

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for("main.manager_dashboard" if user.is_manager else "main.employee_dashboard"))
        flash("Invalid email or password.")
    return render_template("login.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        role = request.form.get("role")
        
        # Validation
        if not email or not username or not password or not confirm_password or not role:
            flash("All fields are required.")
            return render_template("register.html")
        
        if password != confirm_password:
            flash("Passwords do not match.")
            return render_template("register.html")
        
        if len(password) < 6:
            flash("Password must be at least 6 characters long.")
            return render_template("register.html")
        
        if role not in ['manager', 'employee']:
            flash("Please select a valid role.")
            return render_template("register.html")
        
        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash("Email already registered.")
            return render_template("register.html")
        
        if User.query.filter_by(username=username).first():
            flash("Username already taken.")
            return render_template("register.html")
        
        # Create new user
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash("Registration successful! You can now log in.")
        return redirect(url_for('main.login'))
    
    return render_template("register.html")

@main.route("/manager_dashboard", methods=["GET", "POST"])
@login_required
def manager_dashboard():
    if not current_user.is_manager:
        flash("Access denied. Manager privileges required.")
        return redirect(url_for('main.employee_dashboard'))
    
    if request.method == "POST":
        message_content = request.form.get("message")
        message = Message(content=message_content, user_id=current_user.id)
        db.session.add(message)
        db.session.commit()
        flash("Message sent to all employees.")
    messages = Message.query.filter_by(user_id=current_user.id).all()
    return render_template("manager_dashboard.html", messages=messages)

@main.route("/employee_dashboard", methods=["GET", "POST"])
@login_required
def employee_dashboard():
    if current_user.is_manager:
        flash("Access denied. You are a manager.")
        return redirect(url_for('main.manager_dashboard'))
    
    if request.method == "POST":
        response_content = request.form.get("response")
        message_id = request.form.get("message_id")
        message = Message.query.get(message_id)
        if message:
            # Note: The current Message model doesn't have a responses field
            # This would need to be implemented if response functionality is needed
            flash("Response functionality not yet implemented.")
    messages = Message.query.all()
    return render_template("employee_dashboard.html", messages=messages)

@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))
