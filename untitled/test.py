from flask import Flask,request
from flask_restful import Api, Resource,reqparse
import pyodbc
import os

class ConnectionHelper:
    def get_connection(self):
             conn = pyodbc.connect('Driver={SQL Server};'
                'Server=-DESKTOP-5RKIGS9\SQLEXPRESS;'
                'Database=python;'
                'Trusted_Connection=yes;')
             my_cursor = conn.cursor() # type: object

             #print(conn)
             return conn, my_cursor



