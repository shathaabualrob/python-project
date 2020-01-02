from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
import pyodbc
import os


class insert_user(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id", required=True, type=int)
        parser.add_argument("Name", required=True)
        parser.add_argument("Age",required=True)
        parser.add_argument("Country",required=True)
        parser.add_argument("Email",required=True)
        parser.add_argument("Password",required=True)
        content = parser.parse_args()
        connection, cursor = ConnectionHelper().get_connection()
        query = "insert into User(Id,name,Country,Age,Email,Password) values(" + str(content["Id"]) + ",'" + str(content["Name"]) + ",'" + str(content["Age"]) +",'" + str(content["Country"]) + ",'" + str(content["Email"]) +",'" + str(content["Password"]) +"')"
        cursor.execute(query)
        connection.commit()





