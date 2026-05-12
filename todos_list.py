from app import app, db, Todo

def run():
    with app.app_context():
        first_todo = Todo(todo_list="Build web app")
        db.session.add(first_todo)
        db.session.commit()
        all_todos = Todo.query.all()
        print(all_todos)

if __name__ == "__main__":
    run()