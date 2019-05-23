from app_init import app
from flask_pymongo import PyMongo
from bson import json_util
import json


app.config['MONGO_URI'] = 'mongodb://localhost:27017/book'
mongo = PyMongo(app)


class JdBooks:
    @staticmethod
    def jd_with_rank():
        book_li = mongo.db.BookJD.find({}, {'_id': 0}).sort([('rank', 1)]).limit(10)
        result = json.loads(json_util.dumps(book_li))
        return result

    @staticmethod
    def jd_with_title_param(title):
        book_li = mongo.db.BookJD.find_one_or_404({'$or': [{'title': {'$regex': title}}]}, {'_id': 0})
        result = json_util.dumps(book_li)
        return result


class BooksChina:
    @staticmethod
    def china_with_rank():
        book_li = mongo.db.BooksChina.find({}, {'_id': 0}).sort([('rank', 1)]).limit(10)
        result = json.loads(json_util.dumps(book_li))
        return result

    @staticmethod
    def china_with_title_param(title):
        book_li = mongo.db.BooksChina.find_one_or_404({'$or': [{'title': {'$regex': title}}]}, {'_id': 0})
        result = json_util.dumps(book_li)
        return result


class DangBooks:
    @staticmethod
    def dang_with_rank():
        book_li = mongo.db.DangDang.find({}, {'_id': 0}).sort([('rank', 1)]).limit(10)
        result = json.loads(json_util.dumps(book_li))
        return result

    @staticmethod
    def dang_with_title_param(title):
        book_li = mongo.db.DangDang.find_one_or_404({'$or': [{'title': {'$regex': title}}]}, {'_id': 0})
        result = json_util.dumps(book_li)
        return result
