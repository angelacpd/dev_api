from flask import Flask, request, jsonify
import json


app = Flask(__name__)


tasks = [
    {
        'id': 0,
        'assignee': 'Raphael',
        'task': 'Develop method GET',
        'status': 'done'
    },
    {
        "id": "1",
        "assignee": "Angela",
        "task": "Develop method POST",
        "status": "doing"
    },
    {
        "id": "2",
        "assignee": "Joseph",
        "task": "Develop method PUT",
        "status": "to do"
    }
]


# List all tasks. Insert new task.
@app.route('/tasks/', methods=['GET', 'POST'])
def task():
    if request.method == 'GET':
        return jsonify(tasks)
    if request.method == 'POST':
        data_in = json.loads(request.data)
        position = int(tasks[len(tasks) - 1]["id"]) + 1
        data_in["id"] = position
        tasks.append(data_in)
        message = "Task created. id = {}".format(position)
        return {"status": "Success!", "message": message}


# Edit task. Delete task. Show error message if task id does not exist.
@app.route('/tasks/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def task_id(id):
    if request.method == 'PUT':
        data_in = json.loads(request.data)
        tasks[id]["status"] = data_in["status"]
        message = "Task {} updated.".format(id)
        return jsonify({"status": "Success!", "message": message})
    if request.method == 'DELETE':
        tasks.pop(id)
        message = "Task deleted."
        return jsonify({"status": "Success!", "message": message})
    if request.method == 'GET':
        try:
            response = tasks[id]
            print(response)
        except IndexError:
            message = "Task ID {} does not exist.".format(id)
            response = {"status": "Error!", "message": message}
        except Exception:
            message = "Unknown error. Contact admin."
            response = {"status": "Error!", "message": message}
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
