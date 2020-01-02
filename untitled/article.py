from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
from login import Login, jwt_required
import pyodbc
import os

class get_article(Resource):
    @jwt_required
    def article(id):
        connection, cursor = ConnectionHelper().get_connection()
        query1 = ""
        query2=""

        cursor.execute(query)
        connection.commit()


