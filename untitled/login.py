from flask import Flask
from flask_restful import Api, Resource,request,reqparse
from test import ConnectionHelper
from flask_jwt_extended import *
import datetime

import os
import pyodbc


class ConnectionHelper:
    def get_connection(self):
             conn = pyodbc.connect('Driver={SQL Server 15.0.2070};'
                'Server=-DESKTOP-5RKIGS9\SQLEXPRESS;'
                'Database=python;'
                'Trusted_Connection=yes;')
             my_cursor = conn.cursor() # type: object

             #print(conn)
             print("amal")
             return conn, my_cursor



class Login(Resource,ConnectionHelper):

    def get(self):
         parser = reqparse.RequestParser()
         parser.add_argument("Email", required=True, type=str)
         parser.add_argument("Password", required=True, type=str)
         content = parser.parse_args()
         user_email = content["Email"]
         user_password = content["Password"]

         login_status = False
         connection, cursor = ConnectionHelper().get_connection()
         query = "select * from User"
         cursor.execute(query)
         users_dic = {}
         all_rows = cursor.fetchall()
         for row in all_rows:
             users_dic[row[4]] = row[5]

         return users_dic


         #login_success = True
         #return user_email






print(__name__)
app = Flask(__name__)
api = Api(app)
api.add_resource(Login, "/login")
app.config['JWT_SECRET_KEY'] = 'AAABBBCCCDDD'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)
# Authorization: Bearer <JWT>
app.run(
    host="0.0.0.0",
    port=9999
)





