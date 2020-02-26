from flask_restful import Resource
from flask import request
import json


list_skills = ['Python', 'Django', 'Flask', 'Java', 'C']


class Skills(Resource):
    def get(self):
        return list_skills

    def post(self):
        data_in = json.loads(request.data)
        skill = data_in['NewSkill']
        list_skills.append(skill)
        message = "New skill inserted: {}".format(skill)
        return {"status": "Success!", "message": message}
