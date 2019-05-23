from app_init import app
from flask import request
from flask_restful import Api, Resource, reqparse
from models import JdBooks, BooksChina, DangBooks
from flask_cors import CORS

api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('bookname')
# Rank


class JdBookListRank(Resource):
    def get(self):
        result = JdBooks.jd_with_rank()
        return result


class DangBookListRank(Resource):
    def get(self):
        result = DangBooks.dang_with_rank()
        return result


class ChinaBookListRank(Resource):
    def get(self):
        result = BooksChina.china_with_rank()
        return result


@app.route('/detail/jd/<string:bookname>', methods=['GET'])
@app.route('/detail/jd/<string:bookname>/', methods=['GET'])
def JdBookDetail(bookname):
    if request.method == 'GET':
        result = JdBooks.jd_with_title_param(bookname)
        return result


@app.route('/detail/dang/<string:bookname>', methods=['GET'])
@app.route('/detail/dang/<string:bookname>/', methods=['GET'])
def DangBookDetail(bookname):
    if request.method == 'GET':
        result = DangBooks.dang_with_title_param(bookname)
        return result


@app.route('/detail/chinabook/<string:bookname>', methods=['GET'])
@app.route('/detail/chinabook/<string:bookname>/', methods=['GET'])
def ChinaBookDetail(bookname):
    if request.method == 'GET':
        result = BooksChina.china_with_title_param(bookname)
        return result


api.add_resource(JdBookListRank, '/rank/jd')
api.add_resource(DangBookListRank, '/rank/dang')
api.add_resource(ChinaBookListRank, '/rank/china')



if __name__ == '__main__':
    CORS(app, supports_credentials=True)
    app.run(debug=True)
