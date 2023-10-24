from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

todos = [{"task": "Sample Todo","done": False}]


@views.route('/')
@login_required
def home():
    return render_template("home.html", todos=todos, user=current_user)

@views.route("/add", methods=["POST"])
def add():
  todo = request.form['todo']
  todos.append({"task": todo, "done":False})
  return redirect(url_for("views.home"))

@views.route("/edit/<int:home>", methods=["GET", "POST"])
def edit(home):
  todo = todos[home]
  if request.method == "POST":
    todo['task'] = request.form["todo"]
    return redirect(url_for("views.home"))
  else:
    return render_template("edit.html", todo=todo, index=home)
  

@views.route("/check/<int:home>")
def check(home):
  todos[home]['done'] = not todos[home]['done']
  return redirect(url_for("views.home"))

@views.route("/delete/<int:home>")
def delete(home):
  del todos[home]
  return redirect(url_for("views.home"))



