import nltk

from test import ConnectionHelper
from flask import Flask,request
from flask_restful import Api, Resource,reqparse
from login import Login, jwt_required
import pyodbc
import os
from nltk.tokenize import RegexpTokenizer,sent_tokenize
from  nltk.stem import PorterStemmer
from nltk.corpus import stopwords

class article_sentences(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("Id", required=True, type=int)
        content = parser.parse_args()
        connection, cursor = ConnectionHelper().get_connection()
        query = "select Content from Article , InterestManagement where Id ="+content["Id"]
        cursor.execute(query)
        article_content = cursor.fetchall()
        art_dic = {}
        Porter_Stemmer = PorterStemmer()
        stemmed_words = []
        reg_tokenizer = RegexpTokenizer('\w+')
        for articles in article_content:
            sentences = sent_tokenize(articles)
            for sentence in sentences:
                
            uniqe_words = set(reg_tokenizer((articles)))
            for word in uniqe_words:









