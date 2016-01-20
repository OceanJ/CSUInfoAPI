#coding=utf-8
from flask import Flask
from flask_restful import Api, Resource,reqparse
from models import *
app=Flask(__name__)
api=Api(app)
class all_locations(Resource):
    def get(self):
        location_list=get_all_locations()
        return location_list

class all_info(Resource):
    def get(self):
        info_list=get_all_infos()
        return info_list


class search_match_string(Resource):
    def get(self,match_string):
        info_list=search_from_string(match_string)
        return info_list


class search_type(Resource):
    def get(self,type):
        info_list=search_from_type(type)
        return info_list

class search_location_id(Resource):
    def get(self,location_id):
        info_list=search_from_location_id(location_id)
        return info_list

parserdate = reqparse.RequestParser()
parserdate.add_argument('begin',type=int,help='请传入有效起始日期 年/月/日 如：20160101')
parserdate.add_argument('end',type=int,help='请传入终止日期 年/月/日 如：20160101')

class search_date(Resource):
    def get(self):
        args=parserdate.parse_args()
        begin=args['begin']
        end=args['end']
        info_list=search_from_date(begin,end)
        return info_list


api.add_resource(all_locations,'/all_locations')
api.add_resource(all_info,'/all_info')
api.add_resource(search_match_string,'/search_match_string/<string:match_string>')
api.add_resource(search_type,'/search_type/<string:type>')
api.add_resource(search_location_id,'/search_location_id/<int:location_id>')
api.add_resource(search_date,'/search_date')

if __name__ == '__main__':
    app.run()
