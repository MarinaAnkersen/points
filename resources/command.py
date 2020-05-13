from flask_restful import  Resource, reqparse
from flask_jwt_extended import (
jwt_required,
jwt_optional,
get_jwt_identity)
from models.command import CommandModel


class Command(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('spi',type=float)
    parser.add_argument('off',type=float)
    parser.add_argument('defi',type=float)
    parser.add_argument('goal_dif',type=int)
    parser.add_argument('pts',type=int)
    parser.add_argument('relegated',type=int)
    parser.add_argument('make_from_playoffs',type=int)
    parser.add_argument('promoted',type=int)
    parser.add_argument('win_championship',type=int)

    # @jwt_required
    def get(self, command_name):
        command = CommandModel.find_by_name(command_name)
        if command:
            return command.json()
        return {'message': 'It doesnt exist '}, 404


    def post(self, command_name):
        if CommandModel.find_by_name(command_name):
            return {'message': "a command '{}' already exists".format(command_name)}, 400
        data = Command.parser.parse_args()
        command = CommandModel(command_name, **data)

        try:
            command.save_to_db()
        except:
            return {"message": "An error has occured"}, 500 #internale server error

        return command.json(), 201


class CommandList(Resource):
    # @jwt_optional
    def get(self):
        # user_id = get_jwt_identity()
        commands = [command.json() for command in CommandModel.find_all()]
        # if user_id:
        #     return {'commands': commands}, 200
        # return {'commands': [command['command_name'] for command in commands],
        # 'message': 'More data available if you log in'}, 200
        return {'commands': commands}



        # {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
