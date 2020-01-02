from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
import pyodbc
import os


class insert_user(Resource):
    def insert_user(id,name,country,age,email,password):
        connection, cursor = ConnectionHelper().get_connection()
        query = "insert into employee(id,name,country,age,email,password) values(" + str(id) + ",'" + name + "')"
        cursor.execute(query)
        connection.commit()





