from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
import pyodbc
import os

class get_article(Resource):
    def article(id):
        connection, cursor = ConnectionHelper().get_connection()
        query = ""
        cursor.execute(query)
        connection.commit()


