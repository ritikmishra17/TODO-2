from app import app, db
from flask import render_template
from model import Todo


@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
