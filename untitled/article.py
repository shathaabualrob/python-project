from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
from login import Login, jwt_required
import pyodbc
import os

class get_article(Resource):
    @jwt_required
    def article(id):
        parser = reqparse.RequestParser()
        parser.add_argument("userid", required=True, type=int)
        content = parser.parse_args()
        user_id = content["userid"]
        connection, cursor = ConnectionHelper().get_connection()
        query1 = "select  Title, Content, Topic from Interest, Article, IntrestManagement where IntrestManagement.Intrest_Id="+ str(content["userid"])
        count=0
        cursor.execute(query1)
        all_rows = cursor.fetchall()
        count += 1
        json =""
        json+="{count="+count+"articles:["
        for row in all_rows:
            json+"{Title = "+row[0]+"\\"+"Content = "+row[1]+"\\"+"Topic = "+row[1]+"\\"+"},"+"\\"
        return json+"]"+"\\"+"}"






