from flask import Flask,request
from flask_restful import Api, Resource,reqparse
import pyodbc
import os

class ConnectionHelper(Resource):
    def get_connection(self):
     conn = pyodbc.connect('Driver={SQL Server};'
        'Server=-DESKTOP5RKIGS9\SQLEXPRESS;'
        'Database=python'
        'Trusted_Connection=yes;')
     my_cursor = conn.cursor() # type: object
     return conn, my_cursor


