from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

# Define the Task model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    priority = db.Column(db.String(50), nullable=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    try:
        due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date() if 'due_date' in data else None
        new_task = Task(
            title=data['title'],
            description=data.get('description'),
            due_date=due_date,
            priority=data.get('priority')
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created successfully', 'task_id': new_task.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
