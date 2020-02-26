from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills


app = Flask(__name__)
api = Api(app)


developers = [
    {
        "id": "0",
        "name": "Angela",
        "skills": ["Python", "SQL", "Matlab", "C", "Ada"]},
    {
        "id": "1",
        "name": "Eric",
        "skills": ["C", "Unix", "Assembly", "Real-Time"]}
]


# Return, edit and delete a developer
class Developer(Resource):
    def get(self, id):
        try:
            response = developers[id]
            print(response)
        except IndexError:
            message = "Developer ID {} does not exist.".format(id)
            response = {"status": "Error!", "message": message}
        except Exception:
            message = "Unknown error. Contact admin."
            response = {"status": "Error!", "message": message}
        return response

    def put(self, id):
        data = json.loads(request.data)
        developers[id] = data
        return data

    def delete(self, id):
        developers.pop(id)
        return {"status": "Success!", "message": "Register deleted."}


# List all developers and allow registering new developer
class ListDevelopers(Resource):
    def post(self):
        data_in = json.loads(request.data)
        position = len(developers)
        data_in['id'] = position
        developers.append(data_in)
        message = "Register inserted. id={}".format(position)
        return {"status": "Success!", "message": message}

    def get(self):
        return developers


api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
