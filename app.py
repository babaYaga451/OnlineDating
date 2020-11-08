from flask import Flask
from flask_restful import Api
from Resources.User import UserRegister, User, UserLogin
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api = Api(app)
jwt = JWTManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret_key'

api.add_resource(UserRegister, '/signup')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(debug=True, port=8080)
