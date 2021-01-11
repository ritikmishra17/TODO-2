from app import app, db
from flask import url_for, redirect, request
from model import Todo


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    desc = request.form.get("desc")
    asdate = request.form.get("asdate")
    prior = request.form.get("prior")
    assignto = request.form.get("assignto")

    new_todo = Todo(title=title, complete=False, desc=desc, asdate=asdate, prior=prior, assignto=assignto)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))
