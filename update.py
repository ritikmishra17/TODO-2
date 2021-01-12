from app import app, db
from flask import url_for, redirect, Blueprint
from model import Todo

update_bp = Blueprint('update_bp', __name__)


@update_bp.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("index"))
