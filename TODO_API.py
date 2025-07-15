from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

tasks = []

class TaskList(Resource):
    def get(self):
        return tasks

    def post(self):
        data = request.json
        tasks.append(data)
        return {"message": "Task added", "task": data}, 201

api.add_resource(TaskList, "/tasks")

if __name__ == "__main__":
    app.run(debug=True)
