import datetime
import os
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import *
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token,get_jwt_identity)
import pyodbc
import spacy
import nltk

articles = {"id": "1", "intrest_id": "223", "title": "hello", "content": "Hello World"}
u = dict(email='shatha@email.com', password='123', id='21511773')
u2 = dict(id="21511773", name="shatha", age="22", country="palestine", email="shatha@email.com",password="123")
users = {("id", "1"), ("name", "shatha"), ("age", "22"), ("country", "palestine"), ("email", "shatha@email.com"),
         ("password", "123")}  # ,
# 2: {"id": "2", "name": "amal", "age": "22", "country": "palestine", "email": "amal@email.com",
# ,[(id", "2"), ("name", "amal"), ("age", "22"), ("country", "palestine"), ("email", "amal@email.com")]
# "password": "456"}}
intrest = {"id": "1", "topic": "hi", "description": "how to say hello"}
employee_dic = {1: "Mohammad", 2: "Ahmad"}


# login_status = False


class Test(Resource):
    def get(self):
        id = request.args.get("employee_id", default=0, type=int)
        return employee_dic[id]


class Login(Resource):
    def get(self):
        login_status = False
        print("before reading input")
        email = request.args.get("email", default=None, type=None)
        password = request.args.get("password", default=None, type=None)
        print("before if")
        if u2["email"] == email:  # if found in email col in users table in db
            if u2["password"] == password:  # if found in password col in users table
                # return u2["email"]
                login_status = True
        print("user verified")
        print(u2["id"])
        if login_status:
            access_token = create_access_token(identity=u2["id"])
            return access_token

        else:
            login_status = False
            return "Login Fails"


class Article(Resource):
    def get(self):
        return print("hi")


# print("hi")
app = Flask(__name__)
app.config["JWT-SECRET-KEY"]="AAABBBCCCDDD"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
api = Api(app)
api.add_resource(Article, "/article")
api.add_resource(Login, "/login")
api.add_resource(Test, "/test")
jwt = JWTManager(app)
# api.add_resource(ConnectionHelper, "/db")
print(os.getenv('LISTEN', '0.0.0.0'))
app.run(
    host="0.0.0.0",
    port=9999
)
