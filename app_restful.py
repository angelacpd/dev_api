from flask import Flask, request
from flask_restful import Resource, Api
import json
from skills import Skills, list_skills


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
        "skills": ["C", "Unix", "Assembly"]}
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
        dev_skills = data_in['skills']
        missing_skills = []

        for dev_skill in dev_skills:
            skill_exists = False
            for skill in list_skills:
                if dev_skill == skill:
                    skill_exists = True
            if not skill_exists:
                missing_skills.append(dev_skill)

        if len(missing_skills) == 0:
            position = len(developers)
            data_in['id'] = position
            developers.append(data_in)
            message = "Register inserted. id={}".format(position)
            status = "Success!"
        else:
            message = "Unable to register developer. Missing skills: {}".format(missing_skills)
            status = "Failure!"

        return {"status": status, "message": message}

    def get(self):
        return developers


api.add_resource(Developer, '/dev/<int:id>/')
api.add_resource(ListDevelopers, '/dev/')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)
