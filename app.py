from flask import Flask, jsonify, request
import json


app = Flask(__name__)


developers = [
    {
        "id": "0",
        "name": "Angela",
        "skills": ["Python", "SQL", "Matlab", "C", "Ada"]},
    {
        "ide": "1",
        "name": "Eric",
        "skills": ["C", "Unix", "Assembly", "Real-Time"]}
]


# Return, edit and delete a developer
@app.route("/dev/<int:id>/", methods=['GET', 'PUT', 'DELETE'])
def dev(id):
    if request.method == 'GET':
        try:
            response = developers[id]
            print(response)
        except IndexError:
            message = "Developer ID {} does not exist.".format(id)
            response = {"status": "Error!", "message": message}
        except Exception:
            message = "Unknown error. Contact admin."
            response = {"status": "Error!", "message": message}
        return jsonify(response)
    elif request.method == 'PUT':
        data = json.loads(request.data)
        developers[id] = data
        return jsonify(data)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({"status": "Success!", "message": "Register deleted."})


# List all developers and allow registering new developer
@app.route("/dev/", methods=['POST', 'GET'])
def list_developers():
    if request.method == 'POST':
        data_in = json.loads(request.data)
        position = len(developers)
        data_in['id'] = position
        developers.append(data_in)
        message = "Register inserted. id={}".format(position)
        return jsonify({"status": "Success!", "message": message})
    elif request.method == 'GET':
        return jsonify(developers)


if __name__ == '__main__':
    app.run(debug=True)
