from app import app, db
from flask import render_template
from model import Todo
from update import update, update_bp
from add import add, add_bp
from delete import delete, delete_bp

app.register_blueprint(delete_bp)
app.register_blueprint(add_bp)
app.register_blueprint(update_bp)

@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
