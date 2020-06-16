from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister (Resource):
    """
    This resource allows users to register by sending a
    POST request with their username and password.
    """
    parser = reqparse.RequestParser()  # parser 2 arguments - username and password
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank.")

    def post(self): # post method - allow users to register
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return{'message': 'A user with that username already exists'}, 400  # if user exist - Bad request

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201  # user does not exist hence created
