from flask import Flask
from flask_restful import Api, Resource,request,reqparse
from test import ConnectionHelper
from flask_jwt_extended import *
import datetime
from login import Login
from test import ConnectionHelper
import os
import pyodbc


class search_article(Resource,ConnectionHelper):
    @jwt_required
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("keyword", required=True, type=str)
        content = parser.parse_args()
        keyword = content["keyword"]
        #str(keyword) = split(keyword)
        #print(keyword.split(","))
        keyword= keyword.split(",")

        connection, cursor = ConnectionHelper().get_connection()
        query = "SELECT Topic,Title,Content from Interest , Article"
        cursor.execute(query)
        count = 0
        all_rows = cursor.fetchall()
        for row in all_rows:
            content = row[3]
            if keyword in content:
                count+=1
                return count, all_rows
            else:
                return "article not found"










print(__name__)
app = Flask(__name__)
api = Api(app)
api.add_resource(search_article, "/searcharticle")
app.config['JWT_SECRET_KEY'] = 'AAABBBCCCDDD'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
jwt = JWTManager(app)
# Authorization: Bearer <JWT>
app.run(
    host="0.0.0.0",
    port=9999
)





