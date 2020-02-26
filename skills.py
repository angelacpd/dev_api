from flask_restful import Resource
from flask import request
import json


list_skills = ['Python', 'Django', 'Flask', 'Java', 'C']


class Skills(Resource):
    def get(self):
        return list_skills

    def post(self):
        # Example data_in:
        # {"NewSkill": "Assembly"}
        data_in = json.loads(request.data)
        skill = data_in['NewSkill']
        list_skills.append(skill)
        message = "New skill inserted: {}".format(skill)
        return {"status": "Success!", "message": message}

    def put(self):
        # Example data_in:
        # {
        #     "id": 1,
        #     "skill": "Ada"
        # }
        data_in = json.loads(request.data)
        position = data_in["id"]
        skill = data_in["skill"]
        list_skills[position] = skill
        message = "Edited skill n. {}.".format(position)
        return {"status": "Success!", "message": message}

    def delete(self):
        # Example data_in:
        # {
        #     "id": 1,
        # }
        data_in = json.loads(request.data)
        position = data_in["id"]
        skill = list_skills[position]
        list_skills.pop(position)
        message = "Skill {} deleted.".format(skill)
        return {"status": "Success!", "message": message}
