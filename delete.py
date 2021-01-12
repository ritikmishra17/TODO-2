from app import app, db
from flask import url_for, redirect, Blueprint
from model import Todo


delete_bp = Blueprint('delete_bp', __name__)


@delete_bp.route("/delete/<int:todo_id>")
def delete(todo_id):
    
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))
