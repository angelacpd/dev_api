from flask_restful import Resource


list_skills = ['Python', 'Django', 'Flask', 'Java', 'C']


class Skills(Resource):
    def get(self):
        return list_skills
