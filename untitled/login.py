from flask import Flask
from flask_restful import Api, Resource,request,reqparse
from test import ConnectionHelper
from flask_jwt_extended import *
import datetime

class login(Resource):

    def get_user(self):
        connection, cursor = ConnectionHelper().get_connection()
        user_id = request.args.get("email",default=None,Type=None)
        user_password = request.args.get("password",default=None,Type=None)
        login_status = False
        query = "select email,password from User"
        cursor.execute(query)
        user_dic = {}
        all_rows = cursor.fetchall()
        for row in all_rows:
            user_dic[row[0]] = row[1]
        #return user_dic
        print(user_dic)

           # if user["id"] == int(user_id) and user["password"] == user_password:

               # login_success = True
           # if login_success == True:

               # access_token = create_access_token(identity=user_id)
            #return access_token





    print(__name__)
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(login, "/login")

    app.config['JWT_SECRET_KEY'] = 'AAABBBCCCDDD'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    jwt = JWTManager(app)
    # Authorization: Bearer <JWT>
    app.run(
        host="0.0.0.0",
        port=8888
    )





